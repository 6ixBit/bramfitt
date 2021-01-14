<template>
  <div>
    <h1 class="title">
      Historical API Calls
    </h1>

    <Table :data="results"/>
    
  </div>
</template>

<script>
import axios from 'axios'
import Table from '@/components/table'

export default {
    name: "History",
    data() {
      return {
        results: []
      }
    },
    components: {
      Table: Table
    },
    methods: {
      async getResults() {
        try {
          let res = await axios.get("http://localhost:5000/db")

          this.results = res.data
        } catch(e) {
          console.log("Failed to get historical API requests from DB")
        }
      }
    },
    async mounted() {
      this.getResults()
    }
}
</script>

<style scoped>
.title {
  @apply text-2xl font-black my-2;
}
 
.result-list {
  @apply mt-8 list-disc;
}

</style>