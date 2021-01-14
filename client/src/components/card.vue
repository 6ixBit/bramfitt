<template>
    <div class="card-container">
        <div class="card" v-for="data in bus" v-bind:key="data.id">
           <h3 class="card-title">{{data.vehicle_num_plate}}</h3> 
          
           <p class="card-text-item">Direction: {{data.bus_direction}}</p>
           <p class="card-text-item">Station Name: {{data.station_name}}</p>
           <p class="card-text-item">Destination: {{data.destination_name}}</p>
           <p class="card-text-item">Towards: {{data.towards}}</p>
           <p class="card-text-item">Arrival time: {{data.expected_arrival}}</p>
           
        </div>
    </div>
</template>

<script>
export default {
   name: "card",
   props: ["bus"]
}
</script>

<style scoped>
    .card-container {
        @apply flex flex-col justify-center items-center;
    }
   .card {
       @apply border-solid my-2 border-4 rounded-lg w-72 md:w-80 lg:w-96 shadow-lg;
   } 
   .card-title {
       @apply flex justify-center text-center mb-4 font-sans font-bold bg-yellow-300;
   }

   .card-text-item {
       @apply px-4 flex justify-start my-2 font-medium;
   }
</style>