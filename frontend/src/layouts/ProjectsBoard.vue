<template>
    <div class="projects-board">
        <div class="board">
            <ProjectCard 
                v-for = "proj in projects" 
                :key="proj.id" 
                :project="proj"
                />
        </div>
        <RouterLink v-if="latest" to="/projects" class="projects">Смотреть больше <i></i></RouterLink> 
    </div>
</template>

<script>
import { BASE_URL } from '@/config';
import axios from 'axios';
import ProjectCard from '@/components/ProjectCard.vue';

export default{
    name: "ProjectsBoard",
    data(){
        return { projects: [] }
    },
    components:{
        ProjectCard
    },
    props:{
        latest: Boolean
    },
    methods: {
        GET_PROJECTS_FROM_API(){
            let url = BASE_URL;
            if (this.latest){
                url += "projects/latest/";
            }
            else{
                url += "projects/all/";
            }
             
            axios.get(url)
                .then( r => this.projects = r.data)
                .catch( e => console.log(e.response.data.msg))
        },
        redirectToProjects(){
            this.$router.push("/projects")
        }
    },
    mounted(){
        this.GET_PROJECTS_FROM_API()
    }
}
</script>

<style scoped>

.projects-board{
    text-align: right;
    margin-bottom:20px;
}

.board{
    margin: 0 auto 30px;
    display:flex;
    flex-wrap: wrap;
    grid-gap:20px;
    justify-content: space-between;
}

.projects{
    color:white;
    margin:0 1.5%;
    border-bottom:1px solid ;
}
.projects:hover{
    color:var(--main-green);
    border-color:var(--main-green);
    transition: 0.4s;
}
.projects i:after{
    content:"\f061";
    font-style: normal;
    font-family: fa;
}
</style>