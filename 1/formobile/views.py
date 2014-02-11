# -*- coding: utf-8 -*-
from django.http import HttpResponse
from formobile.models import Site, Entry
import simplejson as json

# Create your views here.
def refresh(request):
    print "refreshing"
    for site in Site.objects.all():
    # for site in enumerate(Site.objects.all().iterator()):
        print ".",
        site.refresh_entries()
    print "refreshed"
    return HttpResponse()


def get_by_site(request):
    # if request.GET['site'] and request.GET['page']:
    try:
        """page is an int."""
        site_name = request.GET['site']
        page = int(request.GET['page'])

        entries_in_page = 15

        start_entry_idx = ((page - 1) * entries_in_page)
        end_entry_idx = page * entries_in_page

        s = Site.objects.get(name__exact=site_name)
        entries = Entry.objects.filter(site=s).order_by("-published_ts").values(
            "id", "author", "title", "published", "summary", "content_value", "link").iterator()

        pattern = {
            "site": {},
            "entries": []
        }
        pattern["site"]["name"] = s.name
        pattern["site"]["url"] = s.url

        for idx, val in enumerate(entries):
            if idx in range(start_entry_idx, end_entry_idx):
                pattern["entries"].append(val)

    except KeyError or ValueError:
        pattern = {"404": "Not found."}

    return HttpResponse(json.dumps(pattern, separators=(',', ':'), sort_keys=True))


def get_mixed(request):
    """straightly give you the newest 15 entries mixed up from all sites."""
    entries = Entry.objects.get()
