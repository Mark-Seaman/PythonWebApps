# Data Cascade Design Pattern

## Overview

This design pattern is used with a series of data objects that are nested together to provide varying levels of 
detail.  The data can be represented by an inverted tree structure of objects.

The Data Pattern can illustrated by an outline of nested objects.  Consider the following examples:

## Examples:

### Book

    Book
        Part
            Chapter
                Page
            

### Project Plan

    Developer
        Project
            Milestone
                Task
                    Notes

### Gradebook

    Teacher
        Class
            Student
                Assignment

### Notebook

    Library
        Notebook
            Note
                Comment


### Discussion

This pattern allows us to quickly build an application that uses cascading data.  The way
that the data is processed is common to all of these types of apps.  The core project
structure is built from a set of data models and views.

Each object contains many objects of the next lower item in the cascade.  For the software
project planner this would mean.

* A Developer has several projects
* A Project has serveral Milestones
* A Milestone has serveral Tasks
* A Task has serveral Notes


### Data

The software planner has a cascade of data (Developer Project Milestone Task Notes).

swplan/models.py

    class Developer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
        title = models.CharField(max_length=100)
        body = models.TextField()

        @property
        def projects(self):
            return Project.objects.filter(developer=self)

    class Project(models.Model):
        developer = models.ForeignKey(Developer, on_delete=models.CASCADE, editable=False)
        title = models.CharField(max_length=100)
        body = models.TextField()

        @property
        def milestones(self):
            return Milestone.objects.filter(project=self)

    class Milestone(models.Model):
        project = models.ForeignKey(Project, on_delete=models.CASCADE, editable=False)
        title = models.CharField(max_length=100)
        notes = models.TextField()
        order = models.IntegerField()

        @property
        def tasks(self):
            return Task.objects.filter(milestone=self)

    class Task(models.Model):
        milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, editable=False)
        title = models.CharField(max_length=100)
        notes = models.TextField()


### Views

All five views are created to support the interaction with each data model:

* List
* Detail
* Create
* Edit
* Delete

swplan/views_project.py

    class ProjectListView(ListView):
        template_name = 'project_list.html'
        model = Project
        context_object_name = 'projects'


    class ProjectDetailView(DetailView):
        template_name = 'project_detail.html'
        model = Project
        context_object_name = 'project'

        def get_context_data(self, **kwargs):
            kwargs = super().get_context_data(**kwargs)
            project = kwargs.get('project')
            kwargs.update(dict(milestones=project.milestones))
            return kwargs


    class ProjectCreateView(LoginRequiredMixin, CreateView):
        template_name = "project_add.html"
        model = Project
        fields = '__all__'

        def form_valid(self, form):
            form.instance.developer = Developer.objects.get(user=self.request.user)
            return super().form_valid(form)


    class ProjectUpdateView(LoginRequiredMixin, UpdateView):
        template_name = "project_edit.html"
        model = Project
        fields = '__all__'


    class ProjectDeleteView(LoginRequiredMixin, DeleteView):
        model = Project
        template_name = 'project_delete.html'
        success_url = reverse_lazy('project_list')

