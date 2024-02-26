<template>
    <nav>
        <ul>
            <li v-for="a in nav" :key="a.id">
                <RouterLink :to="a.route"
                            class="nav-link"
                            :class="{ 'is_active_page': isActiveRoute(a.route) }">
                    {{ a.title }}
                </RouterLink>
            </li>
        </ul>
    </nav>
</template>

<script>
import {RouterLink} from 'vue-router'

export default{
    name: "NavBar",
    data(){
        return {
            nav: [ 
                {title:"HOME", route:"/"},
                {title:"ABOUT", route:"/about"},
                {title:"PROJECTS", route:"/projects"},
                {title:"CONTACTS", route:"/contacts"}
            ]
        }
    },
    computed: {
        activeRoute() {
            return this.$route.path;
        }
    },
    methods: {
        isActiveRoute(route) {
            return route === this.activeRoute;
        }
    }

}
</script>

<style scoped>
ul{
    display: flex;
    grid-gap:5px;
}
.nav-link{
    color: var(--main-grey);
    padding:10px;
    font-weight: 300;
    font-size:0.7em;
    letter-spacing: 2px;
}
.nav-link:hover{
    color: white;
    transition: 0.1s;
}
.is_active_page{
    color: var(--main-green);
}
</style>