#!/usr/bin/python3
import cmd
import shlex
import sys
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):

   
    opclas_dic = {
        "BaseModel", "User", "State", "City", "Place", "Amenity",
        "Review"
    }
    prompt = "(hbnb)"
    
    def do_EOF(self, line):
        
        return True

    def do_quit(self, line):
        
        return True
    
   


    def help_quit(self):
       
        print('Quit command to exit the program')

    def help_EOF(self):
       
        print('EOF command to exit the program')

    def emptyline(self):
        
        pass
        
    def do_help(self, linne):
        
        cmd.Cmd.do_help(self, linne)

 


    def do_create(self, linne):
        
        vzgs = shlex.split(linne)

        if len(vzgs) < 1:
            print("** class name missing **")
            return

        class_name = vzgs[0]

        if class_name not in HBNBCommand.opclas_dic:
            print("** class doesn't exist **")
        else:
            cls = globals()[class_name]
            new_inst = cls()
            print(new_inst.id)
            storage.save()
    def do_show(self, linne):
      
        zane_vactor = linne.split()
        if zane_vactor == []:
            print("** class name missing **")
            return
        elif self.opclas_dic.get(zane_vactor[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(zane_vactor) != 2:
            print("** instance id missing **")
            return
        objects_class = storage.all()
        key = zane_vactor[0] + "." + zane_vactor[1]
        if key in objects_class.keys():
            print(objects_class[key].__str__())
        else:
            print("** no instance found **")
            return
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
            instann_dict = storage.all()  
            del instann_dict["{}.{}".format(vrgs[0], vrgs[1])]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, linne):
 

        vrgs = shlex.split(linne)
        if len(vrgs) > 0 and vrgs[0] not in HBNBCommand.opclas_dic:
            print("** class doesn't exist **")
            return

        obj_list = []

        inst_dict = storage.all()
        for key in inst_dict:
            inst = inst_dict[key]

            if len(vrgs) == 0 or (len(vrgs) > 0 and
                                  vrgs[0] == inst.__class__.__name__):
                obj_list.append(inst_dict[key].__str__())
        print(obj_list)
        
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
                class_naims, inst_id = key.split(".")
                validd_idss.append(inst_id)
                if id in validd_idss:
                    obj = objects_dict[f"{class_naims}.{id}"]
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
        class_naims = linne
        all_insta = storage.all()
        for key, obj in all_insta.items():
            name = key.split(".")
            if name[0] == class_naims:
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
