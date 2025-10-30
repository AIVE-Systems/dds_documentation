======================
Protocol v2 Proposal
======================

Recap of Current System
========================

Currently, messages are constructed using a FlatBuffer table. Almost always, this begins with a 64-bit Unix timestamp to indicate when the message was serialised. This is included even though Zenoh appends a timestamp to each ``Sample``; the reason for this is to make the protocol DDS-agnostic, allowing for greater flexibility at the cost of an extra 8-bytes in the message. Often this timestamp is followed by an aircraft/asset type enum, e.g. FSA, STA, FIRE, etc., followed by an 8-bit type-specific ID. The successive fields are then message-dependent.

``asset_speed.fbs`` Visualisation
----------------------------------

+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+------+-----+-----------+-----------+-----------+-----------+
| B1            | B2            | B3            | B4            | B5            | B6            | B7            | B8            | B9   | B10 | B11       | B12       | B13       | B14       |
+===============+===============+===============+===============+===============+===============+===============+===============+======+=====+===========+===========+===========+===========+
| Timestamp 1/8 | Timestamp 2/8 | Timestamp 3/8 | Timestamp 4/8 | Timestamp 5/8 | Timestamp 6/8 | Timestamp 7/8 | Timestamp 8/8 | Type | ID  | Speed 1/4 | Speed 2/4 | Speed 3/4 | Speed 4/4 |
+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+------+-----+-----------+-----------+-----------+-----------+

.. note::
   This does not mean the FlatBuffers byte array is 14 bytes, due to packing and padding systems.

Message v2 Proposal
===================

The idea of the version two of the protocol is to improve the ease of decoding messages. This would split a message into two parts, a header and a payload. The header would contain a 64-bit Unix timestamp, an enum indicating the message type, the device type of the sender, and the ID of the sender. The payload would then contain the message-specific fields, e.g. a speed float, or a fire class (possible or confirmed) and latitude, longitude and altitude fields. This would enable decoding to be done without mapping to topics, not only would this improve the usability of the library, but it would also improve the robustness to error as messages sent on the wrong topic could still be decoded if needed. As the header would be a fixed number of bytes (8 + 1 + 1 + 1 = 11 Bytes), the decoding system would take the first 11 bytes (or the specific header size) of the message and deserialise that into a 4-tuple (using FlatBuffers); the message type would then be used to map to a decoding function.

When encoding such a message, the system will receive the required parameters as arguments, as it does currently, and then encode the header using a centralised header encoder, then the payload would be serialised using message-specific encoders. For decoding, the first 11 bytes would be sliced, decoded separately, and then the message type field would be matched to message-specific decoding functions.

This would have several benefits:

* Improved robustness to unexpected message types
* Identification of senders
* More maintainable encoding/decoding
* Usability improvements to the library

  * Users won't need to carry the topic around their software
  * Users don't need to update the library for new topics—only new message types

The main drawback is the minimal increase in message size (1 Byte best-case). For example, compare this updated message structure with the one above. This will also obviously be a breaking change and would require users to rewrite their function calls with an additional argument.

+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+--------------+-------------+-----+-----------+-----------+-----------+-----------+
| Header        | →             | →             | →             | →             | →             | →             | →             | →            | →           | →   | Payload   | →         | →         | →         |
+===============+===============+===============+===============+===============+===============+===============+===============+==============+=============+=====+===========+===========+===========+===========+
| B1            | B2            | B3            | B4            | B5            | B6            | B7            | B8            | B9           | B10         | B11 | B12       | B13       | B14       | B15       |
+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+--------------+-------------+-----+-----------+-----------+-----------+-----------+
| Timestamp 1/8 | Timestamp 2/8 | Timestamp 3/8 | Timestamp 4/8 | Timestamp 5/8 | Timestamp 6/8 | Timestamp 7/8 | Timestamp 8/8 | Message Type | Device Type | ID  | Speed 1/4 | Speed 2/4 | Speed 3/4 | Speed 4/4 |
+---------------+---------------+---------------+---------------+---------------+---------------+---------------+---------------+--------------+-------------+-----+-----------+-----------+-----------+-----------+
