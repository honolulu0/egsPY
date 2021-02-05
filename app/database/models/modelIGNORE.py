from ... import db

print('init_db')
'''
@现在不用
@2021.2.3
'''

class Cache(db.Model):
    __tablename__ = 'cache'

    id = db.Column(db.Integer, primary_key=True, info='team_id+part_id')
    cache_data = db.Column(db.String(255))


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    category_basic_name = db.Column(db.String(255), nullable=False)


class DemandPlan(db.Model):
    __tablename__ = 'demand_plan'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.ForeignKey('team.id'), nullable=False, index=True)
    part_id = db.Column(db.ForeignKey('part.id'), nullable=False, index=True)
    primary_id = db.Column(db.ForeignKey('primary.id'), nullable=False, index=True)
    demand_project_id = db.Column(db.ForeignKey('demand_project.id'), nullable=False, index=True)
    location_id = db.Column(db.ForeignKey('location.id'), nullable=False, index=True)
    use_plan_id = db.Column(db.ForeignKey('use_plan.id'), nullable=False, index=True)
    revision_time_id = db.Column(db.ForeignKey('revision_time.id'), nullable=False, index=True)
    demand_num = db.Column(db.Integer, nullable=False)
    orig_request_dedicated_qty = db.Column(db.Integer)
    orig_request_shared_qty = db.Column(db.Integer)

    demand_project = db.relationship('DemandProject', primaryjoin='DemandPlan.demand_project_id == DemandProject.id',
                                     backref='demand_plans')
    location = db.relationship('Location', primaryjoin='DemandPlan.location_id == Location.id', backref='demand_plans')
    part = db.relationship('Part', primaryjoin='DemandPlan.part_id == Part.id', backref='demand_plans')
    primary = db.relationship('Primary', primaryjoin='DemandPlan.primary_id == Primary.id', backref='demand_plans')
    revision_time = db.relationship('RevisionTime', primaryjoin='DemandPlan.revision_time_id == RevisionTime.id',
                                    backref='demand_plans')
    team = db.relationship('Team', primaryjoin='DemandPlan.team_id == Team.id', backref='demand_plans')
    use_plan = db.relationship('UsePlan', primaryjoin='DemandPlan.use_plan_id == UsePlan.id', backref='demand_plans')


class DemandProject(db.Model):
    __tablename__ = 'demand_project'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255))


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(255), nullable=False)
    location_basic_name = db.Column(db.String(255), nullable=False)


class Part(db.Model):
    __tablename__ = 'part'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('category.id'), nullable=False, index=True)
    part_name = db.Column(db.String(255), nullable=False)
    part_num = db.Column(db.String(255), nullable=False )
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    manufacturer = db.Column(db.String(255), nullable=False)

    category = db.relationship('Category', primaryjoin='Part.category_id == Category.id', backref='parts')


class Primary(db.Model):
    __tablename__ = 'primary'

    id = db.Column(db.Integer, primary_key=True)
    primary_key = db.Column(db.String(255))


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255), nullable=False, info='????')
    creat_time = db.Column(db.DateTime, nullable=False)


class RevisionTime(db.Model):
    __tablename__ = 'revision_time'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    team_second_line = db.Column(db.String(255))


class UsePlan(db.Model):
    __tablename__ = 'use_plan'

    id = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.ForeignKey('week.id'), index=True)
    num = db.Column(db.Integer)

    week = db.relationship('Week', primaryjoin='UsePlan.week_id == Week.id', backref='use_plans')


class Week(db.Model):
    __tablename__ = 'week'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    code = db.Column(db.String(255), nullable=False, info='????ABCD')
    project_id = db.Column(db.ForeignKey('project.id'), nullable=False, index=True)

    project = db.relationship('Project', primaryjoin='Week.project_id == Project.id', backref='weeks')
