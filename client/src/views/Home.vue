<template>
  <div>
    <div>
      <h1 class="result-title">TFL Bus Information</h1>
    </div>

    <card />

  </div>
</template>

<script>
import axios from "axios"
import card from "@/components/card"

export default {
  name: 'Home',
  data() {
    return {
      busInfo: []
    }
  },
  components: {
    card
  },
  methods: {
    async getBusInfo() {
      try {
        let res = await axios.get("localhost:5000/api")

        this.busInfo = res.data
      } catch (e) {
        console.log(e)
      }
    }
  },
  async mounted() {
    // Call getBusInfo()
  }
}
</script>

<style scoped>

.result-title {
  @apply flex justify-center font-black text-2xl my-2;
}

</style>
