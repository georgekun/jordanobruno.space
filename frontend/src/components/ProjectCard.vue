<template>
    <RouterLink :to="`/project/${project.id}`" class="project-card">
        <div class="card_image" :style="getBackImagePathStyle"></div>
    </RouterLink> 
</template>

<script>
import { RouterLink } from "vue-router"
export default{
    name:"ProjectCard",
    props:{
       project:Object
    },
    computed:{
        getBackImagePathStyle() {
            return { "background-image": `url(${this.project.main_image})` };
        }
    }
}
</script>

<style scoped>

.project-card{
    display: block;
    width: 320px;
    height: 300px;
    margin:auto;
}
.card_image {
    background-repeat: no-repeat; 
    background-size: cover;
    background-position: center;
    border-radius:3px;
    width:100%;
    height: 100%;
}

@media screen and (max-width: 1050px){
    .project-card{
        width: 90vw;
        height: 60vh;
    }
}

@media screen and (max-width: 500px){
    .project-card{
        width: 90vw;
        height: 30vh;
    }
}
</style>