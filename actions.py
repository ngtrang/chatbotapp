from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionPrice(Action):
    def name(self):
        return 'show_price'

    def run(self, dispatcher, tracker, domain):
        faculty = tracker.get_slot('faculty')
        form = tracker.get_slot('form')
        response = ""
        if form == "bachelor":
            response = "The cost of a course for a bachelor is 90.000 rubles. The time of training is 4 years"
        if form == "master":
            response = "The cost of a course for a master is 119.000 rubles. The time of training is 2 years"
        if form == "Ph.D":
            if faculty == "economic":
                response = "The cost of a course for Ph.D in Economic is 150.000 rubles. The time of training is 3 years"
            else:
                response = "The cost of a course for Ph.D is 150.000 rubles. The time of training is 4 years"
        dispatcher.utter_message(response)
        # return [][SlotSet('location', loc)]
        return[]

class ActionInfoFaculty(Action):
    def name(self):
        return  'info_faculty'

    def run(self,dispatcher, tracker, domain):
        faculty = tracker.get_slot('faculty')
        info = ""
        if faculty == "economic":
            info = "Faculty of economics and business administration - the first faculty of the humanities, was founded in 1994. The faculty was organized due to merger of two chairs offering economic specialties:" \
                   "\"Business, marketing and business administration\", \"World economy and economics\" and chairs of the humanities and natural sciences: \
                \"History, culturology, and sociology\", \"Philosophy\", \"Polytology\", \"Foreign languages\", Physical education\", \"Applied mathematics\".The dean of the faculty is Alexander F. Moskovtsev, a D.Sc. (Economics), professor."
        if faculty == "fevt":
            info = "Presently the faculty is the only educational affiliate in the Lower Volga region that has an official license for training specialists in the field of computers and computing complexes, systems and networks; automated systems of data processing and management information systems; computer-aided design systems; systems of physical electronics and medical physics."
        if faculty == "toa":
            info = "Faculty of automated systems and technological informatics was founded at the same time as the university. In 1930 mechanical faculty including cold metal treatment was set up. Among the university's founders are well-known research workers, doctors of Engineering Science, professors E.A. Satel, G.I. Granovskiy, E.B. Uroviczkiy. During the post-war period (till 1956) faculty was called mechanical and technological, from 1956 to 2013 it was termed as machine-building faculty, In 2013 it was named Faculty of automated systems and technological informatics."
        dispatcher.utter_message(info)
        return[]