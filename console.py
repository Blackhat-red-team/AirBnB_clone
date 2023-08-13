#!/usr/bin/python3
import cmd
import json
import re
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from shlex import split
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def farre(linne):
    chary_brazos = re.search(r"\{(.*?)\}", linne)
    braokza = re.search(r"\[(.*?)\]", linne)
    if chary_brazos is None:
        if braokza is None:
            return [i.strip(",") for i in split(linne)]
        else:
            loxcr = split(linne[:braokza.span()[0]])
            rmal = [i.strip(",") for i in loxcr]
            rmal.append(braokza.group())
            return rmal
    else:
        loxcr = split(linne[:chary_brazos.span()[0]])
        rmal = [i.strip(",") for i in loxcr]
        rmal.append(chary_brazos.group())
        return rmal


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    opclas_dic = {
        "BaseModel", "User", "State", "City", "Place", "Amenity",
        "Review"
    }

    def do_quit(self, linne):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, linne):
        """ function to exit the cmd """
        print()
        return True

    def help_quit(self):
        """ help guide for quit command """
        print('Quit command to exit the program')        
    def do_help(self, linne):
        """overrides help method"""
        cmd.Cmd.do_help(self, linne)


    def help_EOF(self):
        print('EOF command to exit the program')

    def emptyline(self):
        """Empty linne."""
        pass

    def do_create(self, linne):

        if linne == "":
            print("** class name missing **")
        else:
            try:
                myclass = eval(linne + "()")
                myclass.save()
                print(myclass.id)
            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, linne):

        linel = farre(linne)
        objdzyt = storage.all()
        if len(linel) == 0:
            print("** class name missing **")
        elif linel[0] not in HBNBCommand.opclas_dic:
            print("** class doesn't exist **")
        elif len(linel) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(linel[0], linel[1]) not in objdzyt:
            print("** no instance found **")
        else:
            print(objdzyt["{}.{}".format(linel[0], linel[1])])

    def do_destroy(self, linne):

        vrgs = shlex.split(linne)

        if len(vrgs) < 1:
            print("** class name missing **")
            return
        if vrgs[0] not in HBNBCommand.opclas_dic:
            print("** class doesn't exist **")
            return
        if len(vrgs) < 2:
            print("** instance id missing **")
            return

        try:
            instann_dict = storage.all()  # get stores objects as dict
            del instann_dict["{}.{}".format(vrgs[0], vrgs[1])]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, linne):

        mval = farre(linne)
        if len(mval) > 0 and mval[0] not in HBNBCommand.opclas_dic:
            print("** class doesn't exist **")
        else:
            objl = []
            for objxx in storage.all().values():
                if len(mval) > 0 and mval[0] == objxx.__class__.__name__:
                    objl.append(objxx.__str__())
                elif len(mval) == 0:
                    objl.append(objxx.__str__())
            print(objl)

    def do_help(self, linne):
        """overrides help methdd"""
        cmd.Cmd.do_help(self, linne)

    def do_update(self, linne):

        vrgs = shlex.split(linne)
        if len(vrgs) == 0:
            print("** class name missing **")
            return
        elif vrgs[0] not in HBNBCommand.opclas_dic:
            print("** class doesn't exist **")
            return
        elif len(vrgs) == 1:
            print("** instance id missing **")
            return
        elif len(vrgs) == 2:
            print("** attribute name missing **")
            return
        elif len(vrgs) == 3:
            print("** value missing **")
            return

        validd_idss = []
        id = vrgs[1]

        try:

            objects_dict = storage.all()
            for key in objects_dict:
                class_name, inst_id = key.split(".")
                validd_idss.append(inst_id)
                if id in validd_idss:
                    obj = objects_dict[f"{class_name}.{id}"]
                    attr = vrgs[2]
                    value = vrgs[3]
                    setattr(obj, attr, value)
                    storage.save()
                    return
                print("** no instance found **")
                return
        except KeyError:
            print("** no instance found **")

    def do_count(self, linne):

        count = 0
        class_name = linne
        all_insta = storage.all()
        for key, obj in all_insta.items():
            name = key.split(".")
            if name[0] == class_name:
                count += 1
        print(count)

    def default(self, linne):

        revax = re.match(r"(\w+\.\w+)(.*)", linne)
        list_command_args = ["do_show", "do_destroy"]

        if revax:
            grv1 = revax.group(1)
            grv1 = grv1.split(".")
            cls_name = grv1[0]
            methdd_nam = grv1[1]
            fll_methdd_nam = "do_" + methdd_nam
            methdd = getattr(self, fll_methdd_nam)
            if fll_methdd_nam in ["do_all", "do_count"]:
                methdd(cls_name)
            elif fll_methdd_nam in list_command_args:
                """ get id as it is needed for this list of commands
                    if not passed only class name is passed """
                regex1 = re.match(r'\(\"(.*)\"\)', revax.group(2))
                if regex1:
                    id = regex1.group(1)
                    methdd(f"{cls_name} {id}")
                else:
                    methdd(f"{cls_name}")
            elif fll_methdd_nam == "do_update":
                regex1 = re.findall(r'[\w-]+', revax.group(2))
                vrgs = " ".join(regex1)
                methdd(f"{cls_name} {vrgs}")

        else:
            return super().default(linne)


if __name__ == '__main__':
    HBNBCommand().cmdloop()