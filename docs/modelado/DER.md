erDiagram

    USER {
        int id PK
        string name
        string email UNIQUE
        datetime created_at
        datetime updated_at
    }

    PROJECT {
        int id PK
        string name
        string description
        datetime created_at
        datetime updated_at
    }

    TASK {
        int id PK
        string title
        string description
        string status
        int project_id FK
        datetime created_at
        datetime updated_at
    }

    TASK_ASSIGNMENT {
        int id PK
        int user_id FK
        int task_id FK
        datetime assigned_at
    }

    TASK_COMMENT {
        int id PK
        int task_id FK
        string comment
        datetime created_at
    }

    PROJECT ||--o{ TASK : contains
    USER ||--o{ TASK_ASSIGNMENT : assigns
    TASK ||--o{ TASK_ASSIGNMENT : includes
    TASK ||--o{ TASK_COMMENT : has