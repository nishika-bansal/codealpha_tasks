let students = [];

function addStudent(){

    let name = document.getElementById("name").value;
    let roll = document.getElementById("roll").value;
    let course = document.getElementById("course").value;

    students.push({
        name:name,
        roll:roll,
        course:course
    });

    displayStudents();
}

function displayStudents(){

    let table = document.getElementById("studentTable");

    table.innerHTML = "";

    students.forEach((student,index)=>{

        table.innerHTML += `
        <tr>
            <td>${student.name}</td>
            <td>${student.roll}</td>
            <td>${student.course}</td>
            <td>
                <button onclick="deleteStudent(${index})">
                Delete
                </button>
            </td>
        </tr>
        `;
    });
}

function deleteStudent(index){
    students.splice(index,1);
    displayStudents();
}