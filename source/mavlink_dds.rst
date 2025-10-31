MAVLink-DDS Bridge
==================

Overview
--------

The MAVLink-DDS bridge node provides bidirectional translation between MAVLink messages (used by ArduPilot) and DDS topics. Each drone runs its own bridge instance.

Sub-Pages
---------

.. toctree::
   :maxdepth: 1

   drop_payload

Connection Types
----------------

The bridge supports multiple MAVLink connection methods:

**TCP Server** (``tcpin:<addr>:<port>``)
   Creates a TCP server listening for incoming connections from the flight controller.

**TCP Client** (``tcpout:<addr>:<port>``)
   Connects as a TCP client to a flight controller or simulator.

**UDP Server** (``udpin:<addr>:<port>``)
   Creates a UDP server listening for incoming packets.

**UDP Client** (``udpout:<addr>:<port>``)
   Sends UDP packets to a specific address.

**UDP Broadcast** (``udpbcast:<addr>:<port>``)
   Broadcasts UDP packets to a subnet.

**Serial** (``serial:<port>:<baudrate>``)
   Connects via serial port (e.g., ``serial:/dev/ttyACM0:115200``).

Published Topics
----------------

The bridge publishes the following telemetry data:

.. list-table::
   :header-rows: 1
   :widths: 35 45 20

   * - Topic
     - Description
     - Message Type
   * - ``aircraft/[TYPE]/[ID]/position``
     - Global position (lat/lon in degrees, altitude in metres AMSL)
     - ``asset_global_position``
   * - ``aircraft/[TYPE]/[ID]/velocity``
     - Ground velocity vector (m/s)
     - ``asset_velocity``
   * - ``aircraft/[TYPE]/[ID]/heading``
     - Heading in degrees
     - ``asset_heading``
   * - ``aircraft/[TYPE]/[ID]/status``
     - System status
     - ``asset_status``
   * - ``aircraft/[TYPE]/[ID]/attitude``
     - Roll, pitch, yaw
     - ``asset_attitude``
   * - ``aircraft/[TYPE]/[ID]/airspeed``
     - Airspeed
     - ``asset_speed``
   * - ``aircraft/[TYPE]/[ID]/groundspeed``
     - Groundspeed
     - ``asset_speed``
   * - ``aircraft/[TYPE]/[ID]/climbspeed``
     - Vertical speed
     - ``asset_speed``
   * - ``aircraft/[TYPE]/[ID]/local_position``
     - Local position (metres from home)
     - ``asset_local_position``
   * - ``aircraft/[TYPE]/[ID]/mode``
     - Flight controller mode
     - ``aircraft_mode``
   * - ``aircraft/[TYPE]/[ID]/movement_state``
     - Movement state (e.g., ON_GROUND, IN_AIR)
     - ``aircraft_state``
   * - ``aircraft/[TYPE]/[ID]/battery_percentage``
     - The percentage of the battery
     - ``float``
   * - ``aircraft/[TYPE]/[ID]/wind``
     - Wind estimation data
     - ``wind``

Subscribed Topics
-----------------

The bridge subscribes to command topics for flight control:

.. list-table::
   :header-rows: 1
   :widths: 40 40 20

   * - Topic
     - Description
     - Message Type
   * - ``aircraft/[TYPE]/[ID]/set_next_waypoint``
     - Insert waypoint immediately
     - ``aircraft_waypoint``
   * - ``aircraft/[TYPE]/[ID]/add_waypoint``
     - Append waypoint to mission
     - ``aircraft_waypoint``
   * - ``aircraft/[TYPE]/[ID]/set_takeoff``
     - Takeoff and loiter at altitude
     - ``aircraft_takeoff``
   * - ``aircraft/[TYPE]/[ID]/set_landing``
     - Land at specified location
     - ``aircraft_land``
   * - ``aircraft/[TYPE]/[ID]/set_loiter``
     - Loiter at waypoint immediately
     - ``aircraft_waypoint``
   * - ``aircraft/[TYPE]/[ID]/add_loiter``
     - Append loiter waypoint
     - ``aircraft_waypoint``
   * - ``aircraft/[TYPE]/[ID]/add_landing``
     - Append landing waypoint
     - ``aircraft_land``
   * - ``aircraft/[TYPE]/[ID]/set_mission``
     - Replace entire mission
     - ``aircraft_mission``
   * - ``aircraft/[TYPE]/[ID]/clear_mission``
     - Clear all mission items
     - ``bool``
   * - ``aircraft/[TYPE]/[ID]/set_mode``
     - Change flight mode
     - ``aircraft_mode``
   * - ``aircraft/[TYPE]/[ID]/enable_drop``
     - Set the state machine ready to being the drop process
     - ``bool``
   * - ``aircraft/[TYPE]/[ID]/open_payload_bay``
     - Open the payload bay
     - ``bool``
   * - ``aircraft/[TYPE]/[ID]/close_payload_bay``
     - Close the payload bay
     - ``bool``
   * - ``aircraft/[TYPE]/[ID]/drop_payload``
     - Drop the payload
     - ``bool``

Message Filtering
-----------------

High-frequency MAVLink messages can overwhelm the network. The bridge implements configurable filtering for specific message types.

**Configuration Parameters:**

``GPI_PUBLISH_FREQUENCY_HZ``
   Desired publishing frequency for ``GLOBAL_POSITION_INT`` messages.

``GPI_FILTERING_STRATEGY``
   Strategy for selecting which messages to publish:

   - ``FilteringStrategy::LastMessage`` — Publish the most recent message within the interval
   - ``FilteringStrategy::Average`` — Publish an averaged message from all received messages

These parameters are configured in ``src/main.rs`` and require rebuilding to change.

Running the Bridge
------------------

**Prerequisites:**

1. Install `Pixi <https://pixi.sh>`_
2. Initialise submodules: ``git submodule update --init --recursive``
3. Compile FlatBuffers: ``pixi run fbs``

**Building:**

.. code-block:: bash

   # Debug build
   pixi run build debug

   # Release build (recommended)
   pixi run build release

**Execution:**

.. code-block:: bash

   pixi run exec [CONFIG TOML PATH]

   # For deployment
   ./target/release/mavlink_dds_node --config [CONFIG TOML PATH]


SITL Integration
----------------

For development and testing, the bridge integrates with ArduPilot's Software-In-The-Loop simulator.

**Single Instance:**

.. code-block:: bash

   # Start SITL with TCP output
   sim_vehicle.py -v plane --console --map \
                  --out=tcpin:127.0.0.1:5700 \
                  -l 51.501123,-0.142386,6.1,0

   # Start bridge
   pixi run exec STA 28 tcpout:127.0.0.1:5700

**Multiple Instances:**

.. code-block:: bash

   # Start n SITL instances with bridges
   python3 sim_many.py n

   # With custom configuration
   python3 sim_many.py --start_port 5700 \
                       --base_lat 51.5011 \
                       --base_lon -0.1424 \
                       n

This spawns multiple simulators, each with its own bridge instance and unique asset ID.

Physical Hardware
-----------------

**Connection:**

1. Flash ArduPilot firmware using QGroundControl or Mission Planner
2. Connect CubeOrange via USB Micro-B
3. Find device path:

   - Linux: ``ls -l /dev/ttyACM*``
   - macOS: ``ls -l /dev/tty.usbmodem*``

4. Update the config with this MAVLink address

.. note::

  Or set the address in the config to `enumerate` which will try to determine the address at runtime (for physical flight controllers only).

**Troubleshooting:**

- Ensure correct baudrate (typically 57600 or 115200)
- Check user permissions for serial port access
- Verify ArduPilot firmware is correctly flashed
- Monitor MAVLink traffic with ``mavproxy.py`` or QGroundControl

Error Handling
--------------

The bridge handles various failure scenarios:

**Connection Loss**
   Attempts reconnection with exponential backoff.

**Malformed Messages**
   Logs errors but continues processing other messages.

**Invalid Commands**
   Rejects commands that fail validation before sending to flight controller.

**DDS Network Issues**
   Buffers outgoing messages temporarily; drops oldest if buffer fills.

Logging
-------

The bridge logs all translation activities, including:

- MAVLink messages received and published
- DDS commands received and converted
- Connection status changes
- Error conditions

Log verbosity can be controlled via environment variables.
