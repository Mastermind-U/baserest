<template>
    <div align='center'>
        <select v-model="option">
            <option v-for="user in list" :value="user.id" v-bind:key="user.id">
                {{user.attributes.username}}
            </option>
        </select>
        <mu-button @click="addUser">Add</mu-button>
    </div>
</template>

<script>
    export default {
        name: 'AddUsers',
        props: {
            room: '',
        },
        data() {
            return {
                option: '',
                list: '',

            }
        },
        created() {
            this.loadUsers()
        },
        methods: {
            loadUsers() {
                $.ajax({
                    url: 'http://185.159.129.154/api/v1/chat/users/',
                    type: 'GET',

                    success: (response) => {
                        this.list = response.data
                    }
                })
            },
            addUser() {
                $.ajax({
                    url: 'http://185.159.129.154/api/v1/chat/users/',
                    type: 'GET',
                    data: {
                        room: this.room,
                        user: parseInt(this.option),
                    },
                    success: (response) => {
                        alert('Пользователь добавлен!')
                    },
                    error:(response) => {
                        alert('Ошибка!')
                    }
                })
            }
        }
    }
</script>

<style scoped>
</style>