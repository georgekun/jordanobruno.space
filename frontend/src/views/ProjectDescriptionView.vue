<template>
    <div class="project-description">
        <div class="head_text">
            <div>
                <h3>{{ project.type_project || "Не известно" }}</h3>
                <h1>{{ project.title || "Не известно" }}</h1>
            </div>
        </div>

        <!-- <ProjectCard :project = "project"/> -->
        <Cheeps :names="getStackFromProject"></Cheeps>

        <h2>Описание проекта</h2>
        <div class="project_text" v-html="project.full_description"></div>

        <Slider v-if="images.length > 0" :slides="images"></Slider>
    </div>
</template>

<script>
import axios from "axios"
import { BASE_URL } from "@/config";

import ProjectCard from '@/components/ProjectCard.vue';
import Cheeps from '@/components/Cheeps.vue';
import Slider from '@/components/Slider.vue';

export default{
    data(){
        return {
            project:{},
            images:[]
        }
    },
    components:{
        ProjectCard,
        Cheeps,
        Slider
    },
    computed:{
        getStackFromProject(){
            const stringList = this.project.stack;
            if (!stringList){ return [] }
            const list = stringList.split(";")
            return list
        }
    },
    methods:{
        GET_PROJECT_FROM_API(){
            const url = BASE_URL + `projects/${this.project.id}/`
            axios.get(url)
            .then( r => this.project = r.data )
            .catch( e => console.log(e))
        },
        GET_LIST_IMAGES_PROJEC_FROM_API(){
            const url = BASE_URL + `projects/images/${this.project.id}/`
            axios.get(url)
            .then( r => this.images = r.data )
            .catch( e => console.log(e))
        }
    },
    mounted(){
        this.project.id = this.$route.params.id
        this.GET_PROJECT_FROM_API()
        this.GET_LIST_IMAGES_PROJEC_FROM_API()
    }
    
}
</script>

<style scoped>
h3{
    color:var(--main-green);
}
h1{
    max-width: 550px;
}
.head_text{
    min-height: 0;
    margin-top:20vh;
}

.project_text{
    max-width:700px;
    width:100%;
    font-size:17px;
    color: #fff;
    letter-spacing: .5px;
    margin:16px auto;
    font-family: Lato, sans-serif;
    font-weight: 300;
    line-height: 24px;
    display: block;
}
</style>