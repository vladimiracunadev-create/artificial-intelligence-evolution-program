
const REPO_URL = "https://github.com/vladimiracunadev-create/artificial-intelligence-evolution-program";

const state = {
  catalog: null,
  done: new Set(JSON.parse(localStorage.getItem("ai-evolution-progress") || "[]")),
};

function saveProgress() {
  localStorage.setItem("ai-evolution-progress", JSON.stringify([...state.done]));
  updateProgress();
}

function updateProgress() {
  const total = state.catalog?.lesson_count || 0;
  const percent = total ? Math.round(state.done.size / total * 100) : 0;
  document.querySelector("#progress").textContent = `${state.done.size}/${total} · ${percent}%`;
}

function card(lesson) {
  const checked = state.done.has(lesson.id) ? "checked" : "";
  return `
    <article class="card" data-search="${(lesson.title + " " + lesson.keywords.join(" ")).toLowerCase()}" data-kind="${lesson.lab_kind}">
      <div class="meta"><span>${lesson.id}</span><span>${lesson.lab_kind}</span></div>
      <h3>${lesson.title}</h3>
      <p>${lesson.summary}</p>
      <div class="tags">${lesson.keywords.slice(0, 4).map(tag => `<span class="tag">${tag}</span>`).join("")}</div>
      <div class="actions">
        <span>
          <a href="classes/${lesson.id}.html">Abrir clase</a> ·
          <a href="${REPO_URL}/blob/main/${lesson.path}/notebook.ipynb" rel="noopener">📓 Notebook</a>
        </span>
        <label><input class="done" type="checkbox" data-id="${lesson.id}" ${checked}> completada</label>
      </div>
    </article>`;
}

function render() {
  const root = document.querySelector("#catalog");
  root.innerHTML = state.catalog.parts.map(part => `
    <section class="part" data-part="${part.id}">
      <div class="part-head">
        <div><span class="eyebrow">Parte ${part.id}</span><h2>${part.title}</h2></div>
        <p>${part.description}</p>
      </div>
      <div class="grid">${part.lessons.map(card).join("")}</div>
    </section>`).join("");
  root.querySelectorAll(".done").forEach(input => {
    input.addEventListener("change", event => {
      const id = event.target.dataset.id;
      event.target.checked ? state.done.add(id) : state.done.delete(id);
      saveProgress();
    });
  });
  updateProgress();
}

function filter() {
  const query = document.querySelector("#search").value.trim().toLowerCase();
  const kind = document.querySelector("#kind").value;
  document.querySelectorAll(".card").forEach(item => {
    const matchText = !query || item.dataset.search.includes(query);
    const matchKind = !kind || item.dataset.kind === kind;
    item.classList.toggle("hidden", !(matchText && matchKind));
  });
  document.querySelectorAll(".part").forEach(part => {
    part.classList.toggle("hidden", !part.querySelector(".card:not(.hidden)"));
  });
}

fetch("data/catalog.json")
  .then(response => response.json())
  .then(catalog => {
    state.catalog = catalog;
    const select = document.querySelector("#kind");
    [...new Set(catalog.parts.flatMap(part => part.lessons.map(lesson => lesson.lab_kind)))].sort()
      .forEach(kind => select.insertAdjacentHTML("beforeend", `<option value="${kind}">${kind}</option>`));
    render();
    document.querySelector("#search").addEventListener("input", filter);
    select.addEventListener("change", filter);
  });
