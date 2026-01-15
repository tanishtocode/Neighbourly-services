let services = [];


fetch("/services")
  .then(res => res.json())
  .then(data => {
    services = data;
    renderServices(services);
  });


const search = document.getElementById("searchInput");
const category = document.getElementById("categoryFilter");
const locationFilter = document.getElementById("locationFilter");
const availability = document.getElementById("availabilityFilter");

search.addEventListener("input", filterServices);
category.addEventListener("change", filterServices);
locationFilter.addEventListener("change", filterServices);
availability.addEventListener("change", filterServices);

function filterServices() {
  let text = search.value.toLowerCase();
  let cat = category.value;
  let loc = locationFilter.value;
  let avail = availability.value;

  let filtered = services.filter(s => {
    return (
      s.name.toLowerCase().includes(text) &&
      (cat === "all categories" || s.category === cat) &&
      (loc === "All Locations" || s.location === loc) &&
      (avail === "Any Status" || s.availability === avail)
    );
  });

  renderServices(filtered);
}

function renderServices(data) {
  const container = document.getElementById("services-container");
  container.innerHTML = "";

  if (data.length === 0) {
    container.innerHTML = "<h3>No services found</h3>";
    return;
  }

  data.forEach(s => {
    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <p class="status ${s.availability.toLowerCase()}">${s.availability}</p>
      <h2>${s.name}</h2>
      <p class="role">${s.category}</p>
      <p class="location">➤ ${s.location}</p>
      <p class="rating">⭐ ${s.rating}</p>
      <p class="meta">Verified Professional</p>
    `;

    card.onclick = () => {
      window.location.href = `/service/${s.id}`;
    };

    container.appendChild(card);
  });
}

