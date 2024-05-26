<template>
  <div id="app">
    <h1>Planets</h1>
    <ul>
      <li v-for="planet in planets" :key="planet.name">
        <strong>{{ planet.name }}</strong>: {{ planet.description }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      planets: []
    }
  },
  mounted() {
    this.fetchPlanets();
  },
  methods: {
    fetchPlanets() {
      fetch('/api/planets')
        .then(response => response.json())
        .then(data => {
          this.planets = data;
        })
        .catch(error => {
          console.error('Error fetching planets:', error);
        });
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
}
</style>
