User Guide
==========

.. note::

  It is recommended to use :code:`screen` so commands can continue running if terminal windows get closed accidentally (This is especially important on the UAVs).


Ground Station :math:`x`
------------------------

Each of these commands can be run in a new terminal window/tab, or in a screen session.

- **Zenoh Router**

  1. :code:`~/zenoh/zenohd`

- **HARIS**

  1. :code:`cd ~/haris/server/`
  2. :code:`java -jar hut.jar 44101 DDSTest.json`
  3. In the browser, navigate to :code:`http://127.0.0.1:44101`

- **NFOV Receivers**

  1. :code:`cd ~/img_sockets/surv` (Can't remember the exact name)
  2. To receiver images run

     i. IR images: :code:`python3 ir_video.py`
     ii. RGB images: :code:`python3 rgb_video.py`

  3. Run :command:`vlc &` in a shell (this allows launching more than one session)
  4. :kbd:`CTRL/CMD+n` to open a network stream

     i. For the IR stream enter :code:`udp://@:13345`
     ii. For the RGB stream enter :code:`udp://@:13346`

- **WFOV Receivers**

  1. :code:`cd ~/img_sockets/search` (Can't remember the exact name)
  2. To receiver images run

     i. IR images: :code:`python3 ir_video.py`
     ii. RGB images: :code:`python3 rgb_video.py`

  3. Run :command:`vlc &` in a shell (this allows launching more than one session)
  4. :kbd:`CTRL/CMD+n` to open a network stream

     i. For the IR stream enter :code:`udp://@:12345`
     ii. For the RGB stream enter :code:`udp://@:12346`

Troubleshooting
^^^^^^^^^^^^^^^

- **Blank/grey screen in browser**: This can happen if HARIS hasn't loaded fully, leave it a minute and keep refreshing the page.

STA :math:`x`
------------------------

First, ``ssh`` into the UAV by ensuring you are connected to the network (either the mission critical ground network, or the UAV network itself). Navigate to the gateway IP (shown below) and scroll down to the DHCP leases to find the address of the UAV's compute unit.

- Alpha network: ``10.10.0.1``
- Beta network: ``10.20.0.1``
- Gamma network: ``10.30.0.1``
- Delta network: ``10.40.0.1``

Then run :code:`ssh staX@ip`.

- **Zenoh Router**

  1. ``screen -S zenoh``
  2. ``~/zenoh/zenohd``
  3. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  4. Verify it is running with ``screen -ls``

- **MAVLink/DDS Bridge**

  1. ``screen -S mavdds``
  2. ``cd ~/mavlink_dds_compatibility_node``
  3. ``./target/release/mavlink_dds_node --config [config file path]``, e.g. ``--config config_reader/config/sta1.toml``
  4. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  5. Verify it is running with ``screen -ls``

Troubleshooting
^^^^^^^^^^^^^^^

- **No connection to the flight controller**: Check that the config file has the correct MAVLink address, or is set to ``enumerate`` (case sensitive).
- **No messages received**: While the bridge is running, briefly power-cycle the flight controller (not the mission systems). If this still doesn't work, reboot the compute unit. If the address in the config is set to ``enumerate``, try setting the specific address to ``serial:[PORT]:115200`` (the port is likely ``/dev/tty.usbmodemXXXX`` on macOS and ``/dev/ttyACMX`` on Linux).

NFOV
----

First, ``ssh`` into the NFOV sensor by ensuring you are connected to the network (either the mission critical ground network, or the UAV network itself). Navigate to the gateway IP (shown below) and scroll down to the DHCP leases to find the address of the UAV's compute unit.

- Alpha network: ``10.10.0.1``
- Beta network: ``10.20.0.1``
- Gamma network: ``10.30.0.1``
- Delta network: ``10.40.0.1``

Then run :code:`ssh firetirs2-surv1@ip`.

- **IR Sensors**

  1. ``screen -S ir``
  2. ``cd ~/surveillance_instrument/scripts``
  3. ``python3 ir-camera-seek-process.py``
  4. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  5. Verify it is running with ``screen -ls``

- **RGB Sensors**

  1. ``screen -S rgb``
  2. ``cd ~/surveillance_instrument/scripts``
  3. ``python3 picamera2_fps_stream.py``
  4. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  5. Verify it is running with ``screen -ls``

- **Gimble Trackings**

  1. ``screen -S gimble``
  2. ``cd ~/surveillance_instrument/scripts``
  3. ``python3 gimble_tracker.py``
  4. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  5. Verify it is running with ``screen -ls``

Troubleshooting
^^^^^^^^^^^^^^^

- **No movement**: Check the physical setup of the gimble, and check the IR camera is running and writing the ``NumPy`` mask file to the same location the gimble is reading it from.

WFOV
----

First, ``ssh`` into the WFOV sensor by ensuring you are connected to the network (either the mission critical ground network, or the UAV network itself). Navigate to the gateway IP (shown below) and scroll down to the DHCP leases to find the address of the UAV's compute unit.

- Alpha network: ``10.10.0.1``
- Beta network: ``10.20.0.1``
- Gamma network: ``10.30.0.1``
- Delta network: ``10.40.0.1``

Then run :code:`ssh firetirs2-search1@ip`.

- **IR Sensors**

  1. ``screen -S ir``
  2. ``cd ~/search_instrument/scripts``
  3. ``python3 ir-camera-seek-process.py``
  4. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  5. Verify it is running with ``screen -ls``

- **RGB Sensors**

  1. ``screen -S rgb``
  2. ``cd ~/search_instrument/scripts``
  3. ``python3 picamera2_fps_stream.py``
  4. Detach from the session with :kbd:`CTRL+a` (release) and then :kbd:`d`
  5. Verify it is running with ``screen -ls``

Troubleshooting
^^^^^^^^^^^^^^^

- **No connection to the flight controller**: Check the connection between the sensors and the flight controller.
