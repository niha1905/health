const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle"),
      sidebar = body.querySelector("nav"),
      sidebarToggle = body.querySelector(".sidebar-toggle"),
      namesContainer = document.querySelector(".data.names"), // Change to 'namesContainer'
      genderContainer = document.querySelector(".data.gender"); // Change to 'genderContainer'

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark") {
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if (getStatus && getStatus === "close") {
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () => {
    body.classList.toggle("dark");
    if (body.classList.contains("dark")) {
        localStorage.setItem("mode", "dark");
    } else {
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if (sidebar.classList.contains("close")) {
        localStorage.setItem("status", "close");
    } else {
        localStorage.setItem("status", "open");
    }
});
/*
document.addEventListener('DOMContentLoaded', function () {
    // Replace 'YOUR_API_KEY', 'YOUR_BASE_ID', and 'YOUR_TABLE_NAME' with your actual API key, base ID, and table name
    const apiKey = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae';
    const baseId = 'app2WlcjTHxf5aCIZ';
    const tableName = 'smartwatch_data';

    // Construct the Airtable API URL
    const apiUrl = `https://api.airtable.com/v0/${baseId}/${tableName}`;

    // Set up the headers for the API request
    const headers = {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
    };

    // Make the GET request using the Fetch API
    fetch(apiUrl, { headers })
        .then(response => response.json())
        .then(data => {
            // Handle the retrieved data and display it in the HTML page
            const entries = data.records.map(record => ({
                name: record.fields['Name'],
                gender: record.fields['gender']
            }));

            // Populate the name and gender data into the HTML structure
            entries.forEach(entry => {
                const nameElement = document.createElement('span');
                nameElement.className = 'data-list';
                nameElement.textContent = entry.name;
                namesContainer.appendChild(nameElement);

                const genderElement = document.createElement('span');
                genderElement.className = 'data-list';
                genderElement.textContent = entry.gender;
                genderContainer.appendChild(genderElement);
            });
        })
        .catch(error => {
            // Handle any errors that occurred during the fetch
            console.error('Error fetching data:', error);
        });
});
*/

const airtableDataContainer = document.getElementById('airtable-data');

document.addEventListener('DOMContentLoaded', function () {
  // Replace with your actual Airtable API key, Base ID, and table name
  const apiKey = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae';
  const baseId = 'app2WlcjTHxf5aCIZ';
  const tableName = 'smartwatch_data';

  // Construct the Airtable API URL
  const apiUrl = `https://api.airtable.com/v0/${baseId}/${tableName}`;

  // Set up the headers for the API request
  const headers = {
    'Authorization': `Bearer ${apiKey}`,
    'Content-Type': 'application/json',
  };

  // Make the GET request using the Fetch API
  fetch(apiUrl, { headers })
    .then(response => response.json())
    .then(data => {
      const entries = data.records.map(record => ({
        name: record.fields['Name'],
        gender: record.fields['Gender'],
        nursingHome: record.fields['nursing home'],
        phoneNumber: record.fields['Phone Number'], // Assuming you have a "Gender" field
      }));

      entries.forEach(entry => {
        const nameElement = document.createElement('span');
        nameElement.className = 'data-list';
        nameElement.textContent = entry.name;
        airtableDataContainer.appendChild(nameElement);

        const genderElement = document.createElement('span');
        genderElement.className = 'data-list';
        genderElement.textContent = entry.gender;
        airtableDataContainer.appendChild(genderElement);

        const nursingHomeElement = document.createElement('span');
        nursingHomeElement.className = 'data-list';
        nursingHomeElement.textContent = entry.nursingHome;
        airtableDataContainer.appendChild(nursingHomeElement);

        const phoneNumberElement = document.createElement('span');
        phoneNumberElement.className = 'data-list';
        phoneNumberElement.textContent = entry.phoneNumber;
        airtableDataContainer.appendChild(phoneNumberElement);
      });
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      // Handle errors here, e.g., display an error message to the user
    });
});





/*const body = document.querySelector("body"),
      modeToggle = body.querySelector(".mode-toggle");
      sidebar = body.querySelector("nav");
      sidebarToggle = body.querySelector(".sidebar-toggle");

let getMode = localStorage.getItem("mode");
if(getMode && getMode ==="dark"){
    body.classList.toggle("dark");
}

let getStatus = localStorage.getItem("status");
if(getStatus && getStatus ==="close"){
    sidebar.classList.toggle("close");
}

modeToggle.addEventListener("click", () =>{
    body.classList.toggle("dark");
    if(body.classList.contains("dark")){
        localStorage.setItem("mode", "dark");
    }else{
        localStorage.setItem("mode", "light");
    }
});

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    if(sidebar.classList.contains("close")){
        localStorage.setItem("status", "close");
    }else{
        localStorage.setItem("status", "open");
    }
})

//--------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {
    // Replace YOUR_API_KEY and YOUR_BASE_ID with your actual Airtable API key and Base ID
    const apiKey = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae';
    const baseId = 'app2WlcjTHxf5aCIZ';
    const endpoint = `https://api.airtable.com/v0/app2WlcjTHxf5aCIZ/smartwatch_data`;

    AIRTABLE_API_KEY = 'pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae'
AIRTABLE_BASE_ID = 'app2WlcjTHxf5aCIZ'
AIRTABLE_TABLE_NAME = 'smartwatch_data'

    // Fetch data from Airtable
    fetch(endpoint, {
      headers: {
        Authorization: `Bearer pat7hpgmy2itPqWrX.da8a874efe149fc7f8569d6297d44973b6175731bb489123aa14de17b35686ae`,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Update the HTML with Airtable data
        updateData(data.records);
      })
      .catch((error) => console.error('Error fetching data:', error));

    function updateData(records) {
      // Assuming each record in Airtable corresponds to a person
      records.forEach((record, index) => {
        updateElementText(`.data.names .data-list:nth-child(${index + 1})`, record.fields.Name);
        updateElementText(`.data.gender .data-list:nth-child(${index + 1})`, record.fields.Email);
        updateElementText(`.data.joined .data-list:nth-child(${index + 1})`, record.fields.Joined);
        updateElementText(`.data.type .data-list:nth-child(${index + 1})`, record.fields.Type);
        updateElementText(`.data.status .data-list:nth-child(${index + 1})`, record.fields.Condition);
      });
    }

    function updateElementText(selector, newText) {
      const element = document.querySelector(selector);
      if (element) {
        element.textContent = newText;
      }
    }
  });
  */