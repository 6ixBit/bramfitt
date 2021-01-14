<template>
    <div class="card-container">
        <div class="card">
           <h3 class="card-title">Lorem Ipsum</h3> 
           <p class="card-description">
               Ipsum project in lamah indiguos it do not matter,
               money got longer, cars got faster turned to a savage.
               money got longer, cars got faster turned to a savage.
           </p>
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
        @apply flex justify-center my-4;
    }
   .card {
       @apply border-solid border-4 rounded-lg w-72 md:w-80 lg:w-96 shadow-lg;
   } 
   .card-title {
       @apply flex justify-center my-4 font-sans font-bold;
   }
   .card-description {
       @apply flex justify-center px-4 pb-4;
   }
</style>