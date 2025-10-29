Serialisation
=============

Overview
--------

All messages in the DDS network are serialised using FlatBuffers, a cross-platform serialisation library providing efficient binary encoding with zero-copy access. The ``flatbuffer_msg_utils`` library provides message definitions, codecs, and utilities for type-safe communication.

Why FlatBuffers?
----------------

**Zero-Copy Access**
   Data can be accessed directly from the serialised buffer without unpacking, reducing memory allocations and CPU overhead.

**Strong Typing**
   Schema definitions ensure compile-time type safety and prevent incompatible message formats.

**Cross-Language Support**
   Generated code available for Rust, Python, C++, Java, and others, enabling heterogeneous systems.

**Efficiency**
   Minimal serialisation overhead and compact binary encoding suitable for bandwidth-constrained networks.

**Forward/Backward Compatibility**
   Schema evolution allows adding new fields without breaking existing code.

Integration
-----------

**Adding as Submodule:**

.. code-block:: bash

   git submodule add git@github.com:AIVE-Systems/flatbuffer_msg_utils.git msg_utils/
   git submodule update --init --recursive

**Checking Out Stable Version:**

.. code-block:: bash

   cd msg_utils
   git checkout tags/vX.X.X
   cd ..

**Compiling Schemas:**

.. code-block:: bash

   pixi run fbs

This generates Rust bindings from FlatBuffer schemas. Add additional flags for other languages if needed.

Supported Message Types
-----------------------

.. list-table:: Supported Message Types
   :widths: 30 50 20
   :header-rows: 1

   * - Message Name
     - Description
     - File
   * - ``Land``
     - Aircraft ID info and landing information
     - ``aircraft_land.fbs``
   * - ``Mission``
     - Aircraft ID info and a list of mission elements (for takeoff, waypoints, and landing) with ordered parameter tuples
     - ``aircraft_mission.fbs``
   * - ``Takeoff``
     - Aircraft ID info and takeoff information
     - ``aircraft_takeoff.fbs``
   * - ``Waypoint``
     - Aircraft ID info and waypoint information: acceptance radius (32-bit float), pass_radius (32-bit float), latitude (32-bit float), longitude (32-bit float), altitude (32-bit float), autocontinue (Boolean), heading (32-bit float)
     - ``aircraft_waypoint.fbs``
   * - ``Attitude``
     - Aircraft ID info and 3-dimensional roll, pitch and yaw values (32-bit floats)
     - ``asset_attitude.fbs``
   * - ``GlobalPosition``
     - Aircraft ID info and 3-dimensional global position information (32-bit floats)
     - ``asset_global_position.fbs``
   * - ``Heading``
     - Aircraft ID info and a heading value (32-bit float)
     - ``asset_heading.fbs``
   * - ``LocalPosition``
     - Aircraft ID info and 3-dimensional position information (32-bit floats)
     - ``asset_local_position.fbs``
   * - ``Speed``
     - Aircraft ID info and a speed value (32-bit float)
     - ``asset_speed.fbs``
   * - ``Status``
     - Aircraft ID info and a status (stored as an enum for better packing, functions take/return it as a string)
     - ``asset_status.fbs``
   * - ``Velocity``
     - Aircraft ID info and 3-dimensional velocity information (32-bit floats)
     - ``asset_velocity.fbs``
   * - ``Bool``
     - A primitive Boolean value
     - ``bool.fbs``
   * - ``Float``
     - A primitive double-precision (64-bit) float
     - ``float.fbs``
   * - ``Int``
     - A primitive 64-bit (long) integer
     - ``int.fbs``
   * - ``String``
     - A primitive string field
     - ``string.fbs``
   * - ``Wind``
     - Wind prediction data
     - ``wind.fbs``
   * - ``Mode``
     - Aircraft mode information/setting
     - ``aircraft_mode.fbs``
   * - ``State``
     - Aircraft (movement) state information
     - ``aircraft_state.fbs``
   * - ``Radiance``
     - IR radiance values (flattened 3D array of 32-bit floats)
     - ``ir_radiance.fbs``
   * - ``Temperature``
     - IR temperature values (flattened 2D array of 32-bit floats)
     - ``ir_temperature.fbs``
   * - ``Hotspot``
     - IR hotspot values (flattened 2D array of 8-bit unsigned ints)
     - ``ir_hotspot.fbs``

Supported Topics
----------------

.. list-table:: Supported Topics
   :widths: 30 50 20
   :header-rows: 1

   * - Topic Key
     - Description
     - Message Type
   * - ``aircraft/[TYPE]/[ID]/set_next_waypoint``
     - Set the next waypoint for the UAV to navigate to immediately
     - ``aircraft_waypoint.fbs``
   * - ``aircraft/[TYPE]/[ID]/add_waypoint``
     - Add a waypoint to the end of the UAV's mission
     - ``aircraft_waypoint.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_loiter``
     - Set the next waypoint for the UAV to loiter at to immediately
     - ``aircraft_waypoint.fbs``
   * - ``aircraft/[TYPE]/[ID]/add_loiter``
     - Add a waypoint to the end of the UAV's mission to loiter at
     - ``aircraft_waypoint.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_takeoff``
     - Set the UAV to takeoff
     - ``aircraft_takeoff.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_landing``
     - Set the UAV to land
     - ``aircraft_land.fbs``
   * - ``aircraft/[TYPE]/[ID]/add_landing``
     - Set the UAV to land at the end of the mission
     - ``aircraft_land.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_mission``
     - Set a whole mission for the UAV
     - ``aircraft_mission.fbs``
   * - ``aircraft/[TYPE]/[ID]/position``
     - Position information of the UAV
     - ``asset_global_position.fbs``
   * - ``aircraft/[TYPE]/[ID]/local_position``
     - Position information of the UAV in local coordinates
     - ``asset_local_position.fbs``
   * - ``aircraft/[TYPE]/[ID]/velocity``
     - Velocity information of the UAV
     - ``asset_velocity.fbs``
   * - ``aircraft/[TYPE]/[ID]/heading``
     - Heading information of the UAV
     - ``asset_heading.fbs``
   * - ``aircraft/[TYPE]/[ID]/attitude``
     - Attitude information of the UAV
     - ``asset_attitude.fbs``
   * - ``aircraft/[TYPE]/[ID]/status``
     - Status information of the UAV
     - ``asset_status.fbs``
   * - ``aircraft/[TYPE]/[ID]/wind``
     - Wind estimates from the UAV
     - ``wind.fbs``
   * - ``aircraft/[TYPE]/[ID]/wind_sim``
     - Wind estimates from the UAV (simulation)
     - ``wind.fbs``
   * - ``aircraft/[TYPE]/[ID]/airspeed``
     - Airspeed estimate from the UAV
     - ``asset_speed.fbs``
   * - ``aircraft/[TYPE]/[ID]/groundspeed``
     - Groundspeed estimate from the UAV
     - ``asset_speed.fbs``
   * - ``aircraft/[TYPE]/[ID]/climbspeed``
     - Climb speed estimate from the UAV
     - ``asset_speed.fbs``
   * - ``aircraft/[TYPE]/[ID]/plan_drop_waypoint``
     - Trigger FSD drop plan
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/plan_sprint``
     - Trigger sprint plan to head towards drop waypoint
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_sprint``
     - Send over the sprint path to ardupilot through set_mission
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/start_aircraft``
     - Intended to be a physical switch to release the aircraft ConOps autonomous system
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/FST_coordinates``
     - Coordinates of the FST
     - ``asset_global_position.fbs``
   * - ``aircraft/[TYPE]/[ID]/battery_percentage``
     - Battery percentage of the UAV
     - ``float.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_drop_pose``
     - Set the waypoint for payload drop
     - ``aircraft_waypoint.fbs``
   * - ``aircraft/[TYPE]/[ID]/enable_drop_system``
     - Enable the aircraft to perform drop procedure (open/close payload bay, drop, etc)
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/open_payload_bay``
     - Open payload bay doors
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/close_payload_bay``
     - Close payload bay doors
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/payload_bay_state``
     - Status of payload bay doors (opened, closed)
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/time_to_reach_drop``
     - Time to reach drop waypoint
     - ``float.fbs``
   * - ``aircraft/[TYPE]/[ID]/drop_payload``
     - Actuate the payload drop
     - ``bool.fbs``
   * - ``aircraft/[TYPE]/[ID]/set_mode``
     - Set the flight controller mode
     - ``mode.fbs``
   * - ``aircraft/[TYPE]/[ID]/mode``
     - Flight controller mode information
     - ``mode.fbs``
   * - ``aircraft/[TYPE]/[ID]/movement_state``
     - Flight controller movement state information, e.g. IN_AIR, TAKEOFF, etc.
     - ``state.fbs``
   * - ``aircraft/[TYPE]/[ID]/fire/sensor_radiance``
     - Radiance at the sensor for a specific aircraft
     - ``ir_radiance.fbs``
   * - ``aircraft/[TYPE]/[ID]/fire/ground_radiance``
     - Radiance at the ground for a specific aircraft
     - ``ir_radiance.fbs``
   * - ``aircraft/[TYPE]/[ID]/fire/hotspot``
     - Hotspots for a specific aircraft
     - ``ir_hotspot.fbs``
   * - ``aircraft/[TYPE]/[ID]/fire/temperature``
     - Temperature for a specific aircraft
     - ``ir_temperature.fbs``
   * - ``aircraft/[TYPE]/[ID]/fire/metadata``
     - IR Metadata
     - ``string.fbs``

Topic-Message Mapping
----------------------

The ``codec_registry.rs`` file maintains mappings between topic patterns and message types using regular expressions:

.. code-block:: rust

   static TOPIC_MAPPINGS: &[(&str, MessageType)] = &[
       (r"^aircraft/.*/.*/position$", MessageType::GlobalPosition),
       (r"^aircraft/.*/.*/velocity$", MessageType::Velocity),
       (r"^aircraft/.*/.*/set_landing$", MessageType::Land),
       // ... additional mappings
   ];

This enables automatic codec selection based on topic name, ensuring type safety across the system.

Using the Library
-----------------

The library's core utility is its ability to automatically select the correct FlatBuffer codec (encoder/decoder) based on the DDS topic name, ensuring type safety. This is managed by the regular expression mappings in ``codec_registry.rs``.

When sending or receiving a message on a topic like ``aircraft/STA/1/local_position``, the system uses a regular expression match to determine how to encode or decode a message.

Rust Examples
~~~~~~~~~~~~~

To encode a message

.. code-block:: rust

  if let Some(decode_fn) = get_decode_handler(&key_str) {
      match decode_fn(payload_bytes) {
          Ok(decoded_msg) => match decoded_msg {
              DecodedMessage::Takeoff(_ts, _ttype, _id, climb_angle, alt, _autocontinue) => {
                  takeoff(cmd_tx, _mission_rx, true, climb_angle, alt).await
              }
              _ => {
                  warn!("Takeoff callback used on an unknown message type.");
                  Err("Unknown message type".into())
              }
          },
          Err(err) => {
              error!("Error decoding message on {}: {}", key_str, err);
              Err(err.into())
          }
      }
  } else {
      warn!("No handler found for message on {}", key_str);
      Err("No handler found".into())
  }

To decode a message

.. code-block:: rust

  let topic = format!("aircraft/{}/{}/position", ttype, id);
  if let Some(encode_fn) = get_encode_handler(topic.as_str()) {
      let encoded_msg = match encode_fn(EncodeMessageArgs::GlobalPosition {
          ttype: String::from(ttype),
          id,
          latitude: lat,
          longitude: lon,
          altitude: alt,
      }) {
          Ok(msg) => msg,
          Err(err) => {
              error!("Failed to encode message: {}", err);
              return;
          }
      };

      to_send.push((
          topic,
          encoded_msg,
          format!("Latitude: {}, Longitude: {}, Altitude: {}", lat, lon, alt),
      ));
  } else {
      error!("No encoder found for {}", topic)
  }

Python Examples
~~~~~~~~~~~~~~~

To encode a message

.. code-block:: python

    import msg_utils

    lat = 51.5014
    long = 0.1419
    alt = 200

    msg = msg_utils.codings.encode_global_position_msg(
        lat=lat, long=long, alt=alt, type=TYPE, id=ID, topic=TOPIC
    )

To decode a message

.. code-block:: python

    import msg_utils

    payload_dict = msg_utils.codings.decode_msg(payload_bytes, TOPIC)
