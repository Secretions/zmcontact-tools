Zimbra Contact Tools
====================

A suite of console utilities for interfacing with Zimbra contacts, suitable for use with mutt or other similar programs.

Components
----------

NOTE: Many of these are "todo"

* zmcq - Query's contacts, can output in format appropriate to [mutt's query_command](http://www.mutt.org/doc/manual/manual-4.html#query)
* m_zmc - [lbdb](http://www.spinnaker.de/lbdb/) module wrapper for zmcq output
* zmcadd - Add addresses to the address book
* zmc - CLI interface to manage a Zimbra address book

Instructions
------------

For zmcq:

1.) Setup a ~/.zmcrc file with your Zimbra server hostname, account name and password.
2.) Verify it works by manually running a query (ie "zmcq John doe")
3.) In your .muttrc, set the query command to: set query_command = "zmcq %s"

For m_zmc:

1.) Do steps 1 and 2 for zmcq.
2.) Put m_zmc into your lbdb modules dir (or set MODULES_PATH in ~/.lbdbrc)
3.) Add "m_zmc" to your methods in ~/.lbdbrc
