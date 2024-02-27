<template>
    <div class="socials">
        <a target='blank' id='tel' :href="getInfoProfile.number_phone">
            <i class="bi bi-telephone-fill"></i>
        </a>

        <a target='blank' id="mail" :href="getInfoProfile.email">
            <i class="bi bi-envelope-at-fill"></i>
        </a>

        <a target='blank' id='tg' :href="getInfoProfile.github_link">
            <i class="bi bi-github"></i>
        </a>

        <a target='blank' id='git' :href="getInfoProfile.github_link">
           <i class="bi bi-telegram"></i>
        </a> 
    </div>
</template>


<script>
import { mapGetters } from 'vuex';
export default{
    name:'SocialMedia',
    computed:{
        ...mapGetters("main", ['getInfoProfile']),
        

    },
    methods:{
      
    }
}

</script>

<style scoped>
.socials{
    display: flex;
    flex-wrap:wrap;
    /* max-width: 200px; */
    justify-content: left;
    text-align: center;
    overflow: hidden;
    margin:30px 0;
}
a{
    line-height: 1;
    color: rgb(140, 138, 138);
    width: 50px;
    height: 50px;
    display: block;
}
i{
    font-size: 30px;
}
i:hover{
    font-size: 32px;
}
</style>