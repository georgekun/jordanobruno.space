<template>
    <button class="main-btn" @click="handleClick">
        <span v-if="!loading && text">{{ text }}</span>
        <slot v-if = "!loading"></slot>

        <v-progress-circular
            v-else
            width="2"
            size="20"
            indeterminate
        ></v-progress-circular>

    </button>
</template>

<script>
export default{
    name:"MainButton",
    data(){
        return {loading: false}
    },
    props:{
        action: Function,
        text: String
    },
    methods: {
        
        async handleClick() {
            this.loading = true; 
            try {
                await this.action(); 
            }
            finally {
                this.loading = false; 
            }
        }
    }
}
</script>

<style scoped>
.main-btn{
    padding:10px 40px;
    min-width: 200px;
    text-transform: uppercase;
    border: 1px solid var(--main-green);
    color: var(--main-green);
    background-color: inherit;
    cursor: pointer;
    border-radius:4px;
    margin:auto;
}

.main-btn:hover{
    border: 1px solid white;
    color: white;
    transition: .2s;
}
</style>
