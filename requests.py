import matplotlib.pyplot as plt
import sqlite3
import operator

total = 0
all_countries = {}

def requests(total, country):
    count = 0
    crawl = 1
    req_num = 0
    thirdparties = {}
    requests = {}
    temp = "google"
    site = "google"
    for row in cursor:
        
        new = row[1].replace('www.','')
        new = new.replace('https://','')
        new = new.replace('http://','')

        requests[row[0]] = count
        
        if (crawl != row[0]):
            print "ID: ", crawl, " |  Site:", temp, " |  3rd-Party Requests:", count

            total += count
            req_num += count
            
            site = row[2].replace('www.','')
            site = site.replace('https://','')
            site = site.replace('http://','')
            site = site[:-1]
            temp = site
            
            count = 0
            crawl = row[0]
            index = new.find('/')
        
        if (new.find(site) != 0):
            count+=1
            index = new.find('/')

            if (new[:index] in thirdparties):
                thirdparties[new[:index]] = (thirdparties[new[:index]] + 1)
            else:
                thirdparties[new[:index]] = 1

    print "ID: ", crawl, " |  Site:", temp, " |  3rd-Party Requests:", requests[crawl]
    print "Total third-party requests for the top 50 sites in " + country + ": ", req_num

    topsites = requests.items()
    x, y = zip(*topsites)

    plt.plot(x, y)
    plt.xlabel('Visit ID')
    plt.ylabel('Count')
    plt.ylim(ymax=500)
    title = "Count of Third-Party Requests in the Top 50 Sites of " + country
    plt.title(title)
    plt.show()
    return total

def together(total, country):
    count = 0
    crawl = 1
    req_num = 0
    thirdparties = {}
    requests = {}
    temp = "google"
    site = "google"
    for row in cursor:
        
        new = row[1].replace('www.','')
        new = new.replace('https://','')
        new = new.replace('http://','')

        requests[row[0]] = count
        
        if (crawl != row[0]):
            print "ID: ", crawl, " |  Site:", temp, " |  3rd-Party Requests:", count

            total += count
            req_num += count
            
            site = row[2].replace('www.','')
            site = site.replace('https://','')
            site = site.replace('http://','')
            site = site[:-1]
            temp = site
            
            count = 0
            crawl = row[0]
            index = new.find('/')
        
        if (new.find(site) != 0):
            count+=1
            index = new.find('/')

            if (new[:index] in thirdparties):
                thirdparties[new[:index]] = (thirdparties[new[:index]] + 1)
            else:
                thirdparties[new[:index]] = 1

    print "ID: ", crawl, " |  Site:", temp, " |  3rd-Party Requests:", requests[crawl]
    print "Total third-party requests for the top 50 sites in " + country + ": ", req_num

    topsites = requests.items()
    x, y = zip(*topsites)

    plt.plot(x, y)
    plt.xlabel('Visit ID')
    plt.ylabel('Count')
    plt.ylim(ymax=500)
    title = "Count of Third-Party Requests in the Top 50 Sites of " + country
    plt.title(title)
    plt.show()
    return total

###

country = "United States"

print country

conn = sqlite3.connect('us.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

total = requests(total, country)

###

country = "Canada"
print country

conn = sqlite3.connect('can.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

total = requests(total, country)

###

country = "Australia"
print country

conn = sqlite3.connect('aus.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

total = requests(total, country)
total_average = total/3

print "Average amount of third-party requests in non-GDPR countries: ", total_average

all_countries["Non-GDPR"] = total_average

####

country = "United Kingdom"
print country

conn = sqlite3.connect('uk.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

total = requests(0, country)
all_countries[country] = total

####

country = "France"
print country

conn = sqlite3.connect('fr.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

prevtotal = total
total = requests(total, country)
all_countries[country] = total - prevtotal

####

country = "Finland"
print country

conn = sqlite3.connect('fi.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

prevtotal = total
total = requests(total, country)
all_countries[country] = total - prevtotal

####

country = "Germany"
print country

conn = sqlite3.connect('de.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

prevtotal = total
total = requests(total, country)
all_countries[country] = total - prevtotal

####

country = "Netherlands"
print country

conn = sqlite3.connect('nl.sqlite')

cursor = conn.execute("SELECT http_requests.visit_id, http_requests.url, site_visits.site_url \
                       FROM http_requests INNER JOIN site_visits \
                       ON http_requests.visit_id = site_visits.visit_id \
                       ORDER BY http_requests.visit_id")

prevtotal = total
total = requests(total, country)
all_countries[country] = total - prevtotal

total_average = total/5

print "Average amount of third-party requests in non-GDPR countries: ", total_average

all_countries["GDPR"] = total_average

###

display_countries = all_countries.items()
x, y = zip(*display_countries)

plt.plot(x, y)
plt.xlabel('Visit ID')
plt.ylabel('Count')
plt.ylim(ymin=4500,ymax=7000)
plt.xticks(rotation=15)
title = "Total count of third-party requests in the top 50 sites of various countries"
plt.title(title)
plt.show()
    
conn.close()

