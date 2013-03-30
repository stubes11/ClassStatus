##
## :KLHSFDKLSJDLSKFJSDL:KFJDLS:KFJSDL:KJFDL:KJDSL:KFSDJ::LDSKFJ
## aosdjfl;kajsdfl;kajsdl;kfjals;dkjfal;ksdjfal;kdskf
## Created by Kaustubh Kulkarni
##
## March 29, 2013
##
##

import mechanize, cookielib, re, getpass
from bs4 import BeautifulSoup

url = 'https://sims.rutgers.edu/csp/builder.htm?semester=92013#Page_CSPSelectSectionTab'
loginurl = "https://cas.rutgers.edu/login"

class MainBrowser:
    def __init__(self, loginurl):
        self.cj = cookielib.LWPCookieJar()
        self.br = mechanize.Browser()                                ##
        self.br.set_handle_robots(False) # ignore robots             ## Authentication Automation
        self.br.set_cookiejar(self.cj)                               ##
        self.br.set_handle_referer                                   ## 
        self.br.open(loginurl)                                       ##
        self.br.select_form(nr=0)                                    ##
        self.br["username"] = getpass.getpass('Enter username: ')    ##
        self.br["password"] = getpass.getpass('Enter password: ')    ##
        self.br.submit()

    def Openpage(self, url):
        self.wantedpage = self.br.open(url)
        self.content = self.wantedpage.read()

    def CleanHTMLCode(self, html):
        self.soup = BeautifulSoup(html)
        self.code = self.soup.prettify()

    def FindMatches(self, html):
        self.matches = re.findall(r'{"registrationIndex":"(\d+)","legendKey":[^,]+,"sectionNumber":([^,]+),"sectionNotes":[^,]+,"subtitleText":[^,]+,"subtopicText":[^,]+,"sectionEligibility":[^,]+,"specialPermissionAdd":[^,]+,"examCode":[^,]+,"sessionDates":[^,]+,"open":(\w+)',html)

        self.mainlist = []                                                       ##
        for tup in self.matches:                                                 ## Create a list with same elements as search results
            self.mainlist.append([int(tup[0]),tup[1].strip('"'),str(tup[2])])    ##

        self.finallist = []                                  ##                                                         
        for elem in self.mainlist:                           ## Remove duplicates from mainlist
            if elem not in self.finallist:                   ##
                self.finallist.append(elem)

    def PrintAvailability(self, finallist):
        
        self.AdvCellIndex = [25020]
        self.CompSciIndex = [20216,29594,29308,29304,29303,29309,29316,24114,29318,31897,24115,29314,29752,29753,29756,31432,33040,36933,36934,37445,37446,37449,37450]
        self.MetaIndex = [29398]
        self.PlatoIndex = [30572]
        self.LogicIndex = [37855]
        self.MusicIndex = [34755,34776,34777,34778,34779,34780,34781,34782,34783]
        
        for elem in self.finallist:
            if elem[0] in self.AdvCellIndex:
                print ('Class: Adv Cell Bio').ljust(20), 'Index:', elem[0], '   Section Num:', elem[1], '  Open?', elem[2]
            elif elem[0] in self.CompSciIndex:
                print ('Class: Comp Sci').ljust(20), 'Index:', elem[0], '   Section Num:', (elem[1]), '  Open?', elem[2]
            elif elem[0] in self.MetaIndex:
                print ('Class: Metaphysics').ljust(20), 'Index:', elem[0], '   Section Num:', (elem[1]), '  Open?', elem[2]
            elif elem[0] in self.PlatoIndex:
                print ('Class: Aristotle').ljust(20), 'Index:', elem[0], '   Section Num:', (elem[1]), '  Open?', elem[2]
            elif elem[0] in self.LogicIndex:
                print ('Class: Logic').ljust(20), 'Index:', elem[0], '   Section Num:', (elem[1]), '  Open?', elem[2]
            elif elem[0] in self.MusicIndex:
                print ('Class: Music Theory').ljust(20), 'Index:', elem[0], '   Section Num:', (elem[1]), '  Open?', elem[2]
            else:
                print 'There is an unknown index.'

def Main():
    browser = MainBrowser(loginurl)
    browser.Openpage(url)
    browser.CleanHTMLCode(browser.content)
    browser.FindMatches(browser.code)
    browser.PrintAvailability(browser.finallist)

if __name__ == '__main__':
    print 'Running script...\n'
    Main()
    print '\nScript complete.\n'
            
