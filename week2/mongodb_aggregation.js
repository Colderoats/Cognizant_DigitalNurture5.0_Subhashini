db.employee.insertMany([
    {
        emp_id: 1,
        emp_name: "Harshitha",
        department: "IT",
        salary: 50000
    },
    {
        emp_id: 2,
        emp_name: "Rahul",
        department: "HR",
        salary: 40000
    },
    {
        emp_id: 3,
        emp_name: "Priya",
        department: "IT",
        salary: 60000
    },
    {
        emp_id: 4,
        emp_name: "Kiran",
        department: "Finance",
        salary: 45000
    }
]);


db.employee.aggregate([
    {
        $match: {
            department: "IT"
        }
    },
    {
        $project: {
            _id: 0,
            emp_name: 1,
            salary: 1
        }
    }
]);