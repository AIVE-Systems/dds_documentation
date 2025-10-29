Payload Drop System
===================

Overview
--------

The payload drop system enables controlled release of payloads during flight through servo-actuated mechanisms. This functionality is integrated into the MAVLink-DDS bridge and configured via the TOML configuration file.

.. graphviz:: resources/drop_state_machine.dot


Configuration
-------------

Payload drop parameters are specified in the optional ``[drop]`` section of the configuration file:

.. code-block:: toml

   [drop]
   servo_id = 23
   pwm_open = 1700

**Parameters:**

``servo_id``
   PWM output channel number on the flight controller

``pwm_open``
   PWM value that opens the release mechanism

Release Sequence
----------------

When a drop command is received:

1. Bridge validates servo configuration exists
2. MAVLink ``COMMAND_LONG`` message sent with ``MAV_CMD_DO_SET_SERVO``
3. Servo moves to ``pwm_open`` position

Future Enhancements
-------------------

Potential improvements to the payload drop system:

- Confirmation feedback from flight controller
- Add drop waypoints to mission
