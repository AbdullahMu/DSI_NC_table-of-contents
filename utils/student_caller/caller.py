import os
import numpy as np
from random import shuffle
from subprocess import call

class StudentCaller(object):

    dir_path            =   os.path.dirname(os.path.realpath(__file__))
    theme_songs         =   False
    soundclips_dir      =   "/soundclips/soundclips_clean/" # this directory is relative to the student caller directory
    soundfiles          =   []
    player_bin          =   "/usr/bin/afplay"
    students            =   []
    absent_students     =   []
    active_students     =   []
    resource_defaults   =   {
        'questions':    'questions.txt',
        'students':     'students.txt ',
    }

    def __init__(self, ask_questions=False, **options):

        super(StudentCaller, self).__init__()
        
        # Override class defaults if option and with existing class attribute
        for attribute, value in options.items():
            if hasattr(self, attribute):
                print "setting ", attribute
                setattr(self, attribute, value)

        self.ask_questions  =   ask_questions

        if self.ask_questions:
            self.load_resource(resource = "questions", shuffle = True)

        if self.theme_songs:
            self.set_soundclips()

    def set_soundclips(self):
        self.soundfiles = [
            file for file in os.listdir(self.dir_path + self.soundclips_dir) \
            if file[-3:] in ["wav", "mp3"]
        ]

        shuffle(self.soundfiles)

    def set_resource(self, key, value):
        self.resource_defaults[key] = value

    def set_students(self, students):
        """
        Dynamically override an instance of students variables.
        """
        self.students = students

    def set_absent_students(self, absent_students=[]):
        """
        Will remove matching students from student list
        """
        self.students = list(set(self.students) - set(absent_students))

    def load_resource(self, resource='questions', randomize=True):
        """
        Dynamically load class meta-resources and set to class attributes.
        Params: resource str: resource key, shuffle bool: shuffle order of resource items
        """
        with open(self.dir_path + "/" + self.resource_defaults[resource], 'r') as f:
            lines = f.readlines()

        lines = [x.rstrip() for x in lines if not len(x) == 0]
      
        if randomize:
            shuffle(lines)
 
        setattr(self, resource, lines)

    def load_questions(self):
        pass

    def ask_question(self):
        print self.questions.pop()

    def get_student_and_play_theme(self):
        print self.get_student()
        self.play_random_soundfile()

    def get_student(self):
        if len(self.active_students) == 0:
            students = np.repeat(self.students, 2)
            self.active_students = np.random.choice(students,
                                             size=len(students),
                                             replace=False).tolist()

        return self.active_students.pop()

    def play_random_soundfile(self):
        if len(self.soundfiles) == 0:
            files = np.repeat(self.students, 2)
            self.soundfiles = np.random.choice(soundfiles,
                                             size=len(soundfiles),
                                             replace=False).tolist()

        selected_file = self.soundfiles.pop()

        print "Playing:  %s " % selected_file
        call([self.player_bin, self.dir_path + self.soundclips_dir + selected_file])

    def __call__(self):
        print self.get_student()

        if self.ask_questions:
            self.ask_question()

