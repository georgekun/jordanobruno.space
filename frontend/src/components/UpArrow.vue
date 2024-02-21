<template>
    <Transition>
        <div v-if="!isAtTop" class="up_arrow">
            <button class="scroll_btn" @click="scrollToTop">
            </button>
        </div>
    </Transition>
</template>

<script>
export default {
    name: "UpArrow",
    data() {
        return {
            isAtTop: true
        };
    },
    methods: {
        scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        },
        checkScrollPosition() {
            this.isAtTop = window.scrollY === 0;
        }
    },
    mounted() {
        window.addEventListener('scroll', this.checkScrollPosition);
        this.checkScrollPosition();
    },
    beforeDestroy() {
        window.removeEventListener('scroll', this.checkScrollPosition);
    }
};
</script>

<style scoped>
.up_arrow{
    position: fixed;
    right:7%;
    bottom: 10%;
    width: 30px;
    height: 30px;
}
.scroll_btn{
    cursor: pointer;
    background-color: #4b4b4b;
    background-image: url("@/assets/up-arrow.png");
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 100px;
    padding:20px;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>