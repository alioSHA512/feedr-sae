# -*- coding: utf-8 -*-
import feedparser
import time
from django.db import models
# from django_cron import CronJobBase, Schedule
import simplejson as json


class Site(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    url = models.URLField(max_length=200)

    """Store the last_updated time as an attribute of Site. """
    updated_ts = models.FloatField(default=0, editable=True)

    def get_rss_xml(self):
        """Get the raw xml data."""
        return feedparser.parse(self.url)

    def refresh_entries(self):
        xml = self.get_rss_xml()

        # try:
        #     ts_site = time.mktime(xml.updated_parsed)
        # except AttributeError:
        #     print "RSS feed from %s has no attribute 'updated_parsed', using time.time()" % self
        #     ts_site = time.time()

        for entry in reversed(xml.entries):
            """just create entries published after the time. """   
            # try:
            ts_entry = time.mktime(entry.published_parsed)
            ts_old = self.updated_ts
            # except AttributeError:
                # """If the entry does not have attribute published_parsed, we will use the *nix sys. timestamp as its time."""
                # ts_entry = time.time()

            # if ts_site > self.updated_ts:
            if ts_entry > ts_old:
                Entry.objects.create_entry(entry=entry, site=self)
                self.updated_ts = ts_entry

        # self.updated_ts = ts_site
        self.save()

    def __unicode__(self):
        return self.name


class EntryManager(models.Manager):

    """To creat FeedrEntries. 
    According to the django document, a Manager extends models. 
    Manager is usually preferred. """

    def create_entry(self, entry, site):
        new_entry = self.create(site=site)

        # errormsg = formobile.utils.DOESNOT_EXIST_ERROR
        # errormsg = {"errorcode": "500", "errormsg": "The RSS feed does not contain this ttribute."}
        errormsg = "Attribute Doest NOT Exist."

        """My next step is to get rid of these unelegant things. """
        try:
            new_entry.title = entry.title
        except AttributeError:
            print "%s has error with title" % site
            new_entry.title = errormsg

        try:
            new_entry.author = entry.author
        except AttributeError:
            print "%s has error with author" % site
            new_entry.author = errormsg

        try:
            new_entry.published = entry.published
        except AttributeError:
            print "%s has error with published" % site
            new_entry.published = errormsg

        try:
            new_entry.summary = entry.summary
        except AttributeError:
            print "%s has error with summary" % site
            new_entry.summary = errormsg

        try:
            new_entry.content_value = entry.content[0].value
        except AttributeError:
            print "%s has error with content_value" % site
            # new_entry.content_value = "Attribute Doest NOT Exist."
            new_entry.content_value = errormsg

        try:
            new_entry.link = entry.link
        except AttributeError:
            print "%s has error with link" % site
            new_entry.link = errormsg

        new_entry.published_ts = time.mktime(entry.published_parsed)
        new_entry.save()
        return new_entry


class Entry(models.Model):

    """ContentValue from sites. """
    objects = EntryManager()

    site = models.ForeignKey('Site')

    title = models.CharField(max_length=200, default="", editable=True)
    author = models.CharField(max_length=200, default="", editable=True)
    published = models.CharField(
        max_length=60, default="", editable=True)
    summary = models.TextField(default="", editable=True)
    content_value = models.TextField(default="", editable=True)
    link = models.URLField(default="", editable=True)

    published_ts = models.FloatField(default=2, editable=True)

    def __unicode__(self):
        return self.title


# class FeedrCron(CronJobBase):

#     """Extends the CronJobBase, for a cron job. """
#     RUN_EVERY_MINS = 1
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'feedr.feedr_cron'   # an unique code, like a trigger.

#     def do(self):
#         """Everytime you runcrons it will do the refresh_entries function."""
#         for site in Site.objects.all():
#             site.refresh_entries()
