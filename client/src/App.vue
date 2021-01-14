<template>
  <div id="app">
    <nav>
      <router-link to="/" class="nav-item">Home</router-link>
      <router-link to="/history" class="nav-item">History</router-link>
    </nav>

    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}

nav {
  @apply my-8;
}

.nav-item {
  @apply mx-4 rounded-lg underline text-lg text-green-400;
}
</style>
