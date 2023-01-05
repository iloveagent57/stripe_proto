stripe_proto
#############################

.. note::

  This README was auto-generated. Maintainer: please review its contents and
  update all relevant sections. Instructions to you are marked with
  "PLACEHOLDER" or "TODO". Update or remove those sections, and remove this
  note when you are done.

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|

Purpose
*******

stripe prototype

TODO: The ``README.rst`` file should start with a brief description of the repository and its purpose.
It should be described in the context of other repositories under the ``openedx``
organization. It should make clear where this fits in to the overall Open edX
codebase and should be oriented towards people who are new to the Open edX
project.

Getting Started
***************

Developing
==========

One Time Setup
--------------
.. code-block::

  # Clone the repository
  git clone git@github.com:openedx/stripe_proto.git
  cd stripe_proto

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  mkvirtualenv -p python3.8 stripe_proto

Setup with docker devstack
--------------------------

.. code-block::

   # define the stripe test secret key, or put this in your ~/.bash_profile file
   # this is forwarded into the app container's environment, and ultimately
   # into the private.py settings file
   export STRIPE_TEST_SECRET_KEY="..."

   # build and start the app
   make dev.up.build

   # migrate and provision core records
   ./provision-stripe_proto.sh

Add this stuff to your ``private.py`` file.
.. code-block::

   import os
   # https://dj-stripe.dev/dj-stripe/2.7/installation/
   STRIPE_LIVE_SECRET_KEY = None
   STRIPE_TEST_SECRET_KEY = os.environ.get("STRIPE_TEST_SECRET_KEY", "<your secret key>")
   STRIPE_LIVE_MODE = False  # Change to True in production
   DJSTRIPE_WEBHOOK_SECRET = "whsec_xxx"  # Get it from the section in the Stripe dashboard where you added the webhook endpoint
   DJSTRIPE_USE_NATIVE_JSONFIELD = False  # doesn't work on mysql
   DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"


Then you'll probably need to ``make migrate`` from inside the app container again
to get all the djstripe migrations applied.

Now add the API Secret Key from the test account to http://localhost:8321/admin/djstripe/apikey/

Lastly, run ``python manage.py djstripe_sync_models``.  This will sync
every object from the Strip test account to your local database.
Confirm this worked by visiting http://localhost:8321/admin/djstripe/product/
there should be a record for whatever products we have defined in our test account.

Every time you develop something in this repo
---------------------------------------------
.. code-block::

  # Activate the virtualenv
  workon stripe_proto

  # Grab the latest code
  git checkout main
  git pull

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  vim ...

  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit ...
  git push

  # Open a PR and ask for review.

Deploying
=========

TODO: How can a new user go about deploying this component? Is it just a few
commands? Is there a larger how-to that should be linked here?

PLACEHOLDER: For details on how to deploy this component, see the `deployment how-to`_

.. _deployment how-to: https://docs.openedx.org/projects/stripe_proto/how-tos/how-to-deploy-this-component.html

Getting Help
************

Documentation
=============

PLACEHOLDER: Start by going through `the documentation`_.  If you need more help see below.

.. _the documentation: https://docs.openedx.org/projects/stripe_proto

(TODO: `Set up documentation <https://openedx.atlassian.net/wiki/spaces/DOC/pages/21627535/Publish+Documentation+on+Read+the+Docs>`_)

More Help
=========

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the
community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack workspace`_.

For anything non-trivial, the best path is to open an issue in this
repository with as many details about the issue you are facing as you
can provide.

https://github.com/openedx/stripe_proto/issues

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help

License
*******

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to have a discussion about your new feature idea with the maintainers prior to
beginning development to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The assigned maintainers for this component and other project details may be
found in `Backstage`_. Backstage pulls this data from the ``catalog-info.yaml``
file in this repo.

.. _Backstage: https://open-edx-backstage.herokuapp.com/catalog/default/component/stripe_proto

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@tcril.org.

.. |pypi-badge| image:: https://img.shields.io/pypi/v/stripe_proto.svg
    :target: https://pypi.python.org/pypi/stripe_proto/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/openedx/stripe_proto/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/openedx/stripe_proto/actions
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/openedx/stripe_proto/coverage.svg?branch=main
    :target: https://codecov.io/github/openedx/stripe_proto?branch=main
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/stripe_proto/badge/?version=latest
    :target: https://stripe_proto.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/stripe_proto.svg
    :target: https://pypi.python.org/pypi/stripe_proto/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/openedx/stripe_proto.svg
    :target: https://github.com/openedx/stripe_proto/blob/main/LICENSE.txt
    :alt: License

.. TODO: Choose one of the statuses below and remove the other status-badge lines.
.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Deprecated-orange
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Unsupported-red
