Architecture
============

System Overview
---------------

The system architecture is shown below.

.. graphviz:: resources/architecture.dot

Topic Hierarchy
---------------

Topics follow a loose hierarchical naming convention of high level information, specific identification information, then the data stored in that topic, e.g.::

    [HIGH_LEVEL TYPE]/[ASSET_TYPE]/[ASSET_ID]/[DATA_TYPE]

**Components:**

``HIGH_LEVEL TYPE``
   High-level type of asset/information, e.g. `aircraft`.

``ASSET_TYPE``
   Type of asset as a one-byte enum; can be either

   - STA
   - FSA
   - MCS
   - FOB
   - FIRE
   - UNDEFINED

``ASSET_ID``
   Unique 8-bit numerical identifier for the asset (within that type)

``DATA_TYPE``
   Specific data type or command (e.g., ``position``, ``velocity``, ``set_landing``)

**Examples:**

.. code-block:: text

    aircraft/STA/28/position          # Global position data
    aircraft/STA/28/set_next_waypoint # Command to set waypoint
