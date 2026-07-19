import React, { useEffect, useState } from "react";
import { fetchUsers } from "./api";

function UserList() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetchUsers().then(data => setUsers(data));
    }, []);

    return (
        <div>
            <h1>Users</h1>

            <ul>
                {users.map(user => (
                    <li key={user.id}>
                        {user.name}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default UserList;
