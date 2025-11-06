Automated Testing & Deployment
==============================

Automated testing and deployment are useful features aimed at improving system reliability and standardise deployments. We use a combination of GitHub Actions and Jenkins to achieve this.

Currently, few repositories use automated tests/tasks, but adding these to other aspects of the system would be beneficial and help increase code reliability.

.. attention::

    We use both GitHub Actions and Jenkins due to usage limits on GitHub. With the free organisation tier, we are capped on the number of minutes we can use per month. For this reason, testing should be conducted on Jenkins (self-hosted), and deployments on GitHub (for automated compilation on several platforms). For this reason, try to **only use GitHub actions when necessary**.

.. seealso::

    Jenkins is self-hosted by Toby Godfrey and is unavailable to users without an account. For access, request an account directly from him.

``flatbuffer_msg_utils``
------------------------

This repo has two automated processes, ``CI`` and ``Release``.

.. list-table:: Automated Tasks
   :widths: 10 10 10 10 10 40
   :header-rows: 1

   * - Task
     - Category
     - Platform
     - File
     - Trigger(s)
     - Description
   * - CI
     - Testing
     - Jenkins
     - ``Jenkinsfile.ci``
     - Push to ``main``
     - Tests build success in a clean environment, then runs the following:

       - Rust unit tests
       - Rust integration tests
       - Rust unit tests (with Python extension)
       - Rust integration tests (with Python extension)
       - Python tests (Python 3.11)
       - Python tests (Python 3.12)
       - Python tests (Python 3.13)

       In total, approximately 500 tests are executed.
   * - Release
     - Deployment
     - GitHub Actions
     - ``release.yml``
     - New tag created
     - Builds the project on Linux x86_64, Linux AArch64, and macOS AArch64, creates Python wheels for the bindings and adds them to the latest release.

``dds_documentation``
------------------------

This repo has one automated processes, ``Sphinx``.

.. list-table:: Automated Tasks
  :widths: 10 10 10 10 10 40
  :header-rows: 1

  * - Task
    - Category
    - Platform
    - File
    - Trigger(s)
    - Description
  * - Sphinx
    - Documentation
    - GitHub Actions
    - ``sphinx.yml``
    - Push to ``main``
    - Builds the documentation and push to the ``gh-pages`` branch.
