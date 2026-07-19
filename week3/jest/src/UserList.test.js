import { render, screen, waitFor } from "@testing-library/react";
import UserList from "./UserList";
import * as api from "./api";

jest.mock("./api");

test("renders user list from mocked API", async () => {

    api.fetchUsers.mockResolvedValue([
        { id: 1, name: "Alice" },
        { id: 2, name: "Bob" }
    ]);

    render(<UserList />);

    await waitFor(() => {
        expect(screen.getByText("Alice")).toBeInTheDocument();
        expect(screen.getByText("Bob")).toBeInTheDocument();
    });
});