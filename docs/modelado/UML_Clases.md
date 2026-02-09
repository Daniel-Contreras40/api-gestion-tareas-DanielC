classDiagram

class User {
  +int id
  +string name
  +string email
  +string password
  +datetime created_at
  +datetime updated_at
}

class Project {
  +int id
  +string name
  +string description
  +datetime created_at
  +datetime updated_at
}

class Task {
  +int id
  +string title
  +string description
  +date due_date
  +string status
  +datetime created_at
  +datetime updated_at
}

class TaskAssignment {
  +int id
  +datetime created_at
}

class TaskProject {
  +int id
}

User "1" --> "0..*" Task : creates
User "1" --> "0..*" TaskAssignment : assigned
Task "1" --> "0..*" TaskAssignment : has
Project "1" --> "0..*" TaskProject
Task "1" --> "0..*" TaskProject