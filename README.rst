Python graphing artifacts for sysstat data (sar binary format)
==============================================================

Basically a test-bed to see what works for simple time-series of perf
data collected from a modest embedded board running Linux and several
multi-threaded applications.

* candidate 1 - https://github.com/stoneboy100200/sclean
* candidate 2 - https://github.com/pdutton-vc/sarviewer (not really python)
* candidate 3 - https://github.com/jpgxs/python-sadf (archived 2 yrs ago)
* candidate 4 - https://github.com/pafernanr/sarcharts

Run the following Tox_ command to sync the the above candidate repositories
and create a "dev" environment for testing::

  $ tox -e sync
  $ tox -e dev
  $ source .venv/bin/activate


.. _Tox: https://tox.wiki/en/latest/user_guide.html
