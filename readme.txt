docker build -t <name> .
docker run -p 5000:5000 <name>  

Each user can have multiple lists (User.lists).
Each list belongs to a specific user (List.user_id).
Each list can have multiple items (List.items).
Each item belongs to a specific list (ListItem.list_id).



