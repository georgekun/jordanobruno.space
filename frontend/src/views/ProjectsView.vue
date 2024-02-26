<template>
    <div class="projects">
        <div class="head_text">
            <div>
                <h1>Переходите по проектам, <br> чтобы прочитать детальное описание</h1>
            </div>
        </div>
        <ProjectsBoard :latest="false"/>
    </div>
</template>

<script>
import ProjectsBoard from '@/layouts/ProjectsBoard.vue';


export default{
    components:{
        ProjectsBoard, 
        MainButton
    }
}
</script>

<style scoped>
.projects{
    margin-bottom:100px;
}
.head_text{
    min-height: 40vh;
}
.main-button-float{
    display: float;
    float: right;
}

</style>