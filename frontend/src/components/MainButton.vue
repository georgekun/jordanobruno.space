<template>
    <button class="main-btn" @click="action">
        {{ text }}
    </button>
</template>

<script>
export default{
    name:"MainButton",
    props:{
        action: Function,
        text: String
    }
}
</script>

<style scoped>
.main-btn{
    padding:15px 40px;
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
