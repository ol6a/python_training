from model.group import Group
from random import randrange
import random





def test_modify_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="New group3")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    new_group.id = group.id
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group)
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#def test_modify_group_name(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
  #  app.group.modify_first_group(Group(name="New Group"))


#def test_modify_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
  #  app.group.modify_first_group(Group(header="New Header"))
