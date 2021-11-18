# Lesson 24 - Grid System
        
## LEARN

### Office Hours
* If you need help please attend office hours
* MWF  1:30-2:30 by Zoom
* Zoom:   https://unco.zoom.us/j/99180652183
* Email:   mark.seaman@unco.edu      


### Reading for Today  
* Read <a target="_blank" 
href="https://learn.zybooks.com/zybook/UNCOBACS200SeamanFall2021/chapter/4/section/1">
4.1 HTML containers
</a>
* Follow <a target="_blank" href="/course/bacs200/docs/ZybooksReading">Reading Schedule</a>


### Today
* Bootstrap Grid System


### Using Bootstrap
* Link the CSS into the head element

```
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
```


### Bootstrap Navs
* Use class "nav" on list
* Use class "nav-item" on each list item
* Use class "nav-link" on each link element


### Containers
* [Bootstrap Containers](https://www.w3schools.com/bootstrap5/bootstrap_containers.php)
* Use class "container"
* A container builds space on your page

```
<div class="container bg-success text-light">
    <h3>My First Bootstrap Page</h3>
    <p>This is some text.</p>
</div>
```


### Container Fluid
* Allocate full display width
* Use class "container-fluid"

```
<div class="container-fluid bg-primary text-light">
    <h3>My First Bootstrap Page</h3>
    <p>This is some text.</p>
</div>
```


### Grid System
* [Bootstrap Basic Grid](https://www.w3schools.com/bootstrap5/bootstrap_grid_basic.php)
* [Bootstrap Grid System](https://www.w3schools.com/bootstrap5/bootstrap_grid_system.php)
* Use class "row"  to pack items horizontally
* Use class "col"  to size the columns

```
 <div class="row">
      <div class="col">.col</div>
      <div class="col">.col</div>
      <div class="col">.col</div>
</div> 
```


### 12-Column Layout
* Allocate width of columns to hold content
* Wraps at 12
* Example: 2, 6, 4

```
<div class="row">
      <div class="col-2 border">.col-2</div>
      <div class="col-6 border">.col-6</div>
      <div class="col-4 border">.col-4</div>
</div> 
```


### Mixed sizing
* Some numbers with spacing
* Some without
* Extra space in allocate evenly

```
<div class="row">
      <div class="col border">.col</div>
      <div class="col-6 border">.col-6</div>
      <div class="col border">.col</div>
</div> 
```


### Sizing Breakpoints
* sm, md, lg, xl
* [Bootstrap Grid System](https://www.w3schools.com/bootstrap5/bootstrap_grid_system.php)


```
<div class="row">
      <div class="col-md-3 border">.col-md-3</div>
      <div class="col-md-6 border">.col-md-6</div>
      <div class="col-md border">.col-md</div>
</div> 
```



## BUILD


### CSS Demo
* [Demo Code](https://github.com/Mark-Seaman/Mark-Seaman.github.io/tree/master/demo/week9)
* Study code so that you can reproduce these results
* [See Demo on Server](https://Mark-Seaman.github.io/demo/week9/index.html)


### Resources for Learning
* [W3Schools - Bootstrap](https://www.w3schools.com/bootstrap5/default.asp)
* [Bootstrap website](https://getbootstrap.com)
* [Validate the HTML](https://validator.w3.org/)
* [Validate the CSS](http://jigsaw.w3.org/css-validator/)


### Project 9 - Non-profit Blog
* [Project Instructions](/course/bacs200/project/09)

