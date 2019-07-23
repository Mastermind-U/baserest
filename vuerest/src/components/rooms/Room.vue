<template>
    <HomeSlot>
        <mu-row gutter>
            <mu-col span='2'>
                <mu-paper :z-depth="1" style="border: .5px solid black;">
                    <mu-list textline="two-line" :z-depth="1">
                        <div v-for="room in rooms" v-bind:key="room">
                            <div @click="openChat(room.pk)">
                                <mu-list-item button :ripple="false">
                                    <mu-list-item-content>
                                        <mu-list-item-title>
                                            <h4>{{room.creator.username}}</h4>
                                        </mu-list-item-title>
                                        <mu-list-item-sub-title>{{room.date}}</mu-list-item-sub-title>
                                    </mu-list-item-content>
                                </mu-list-item>
                            </div>
                        </div>
                    </mu-list>
                </mu-paper>
                <mu-button @click="addRoom" class="addbtn">Add Room</mu-button>
            </mu-col>
            <mu-col span='10'>
                <slot></slot>
            </mu-col>
        </mu-row>
    </HomeSlot>
</template>
<script>
    import HomeSlot from '@/components/Home'
    export default {
        name: "Room",
        components: {
            HomeSlot
        },
        data() {
            return {
                rooms: '',
            }
        },
        created() {
            $.ajaxSetup({
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                }
            })
            this.loadRoom()

        },
        methods: {
            loadRoom() {
                $.ajax({
                    url: 'http://185.159.129.154/api/v1/chat/room/',
                    type: 'GET',
                    success: (response) => {
                        this.rooms = response.data.data
                    },
                })
            },
            openChat(pk) {
                // this.$emit('openChat', pk)
                this.$router.push({
                    name: 'chat',
                    params: {
                        pk: pk
                    }
                })
            },
            addRoom() {
                $.ajax({
                    url: 'http://185.159.129.154/api/v1/chat/room/',
                    type: 'POST',
                    success: (response) => {
                        this.loadRoom()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            },

        }
    }
</script>
<style scoped>
    ul {
        list-style-type: none;
    }

    .addbtn {
        width: 100%;
    }
</style>