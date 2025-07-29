import { View, Image, StyleSheet, TouchableOpacity } from "react-native"
import { useNavigation, DrawerActions, DrawerStatus } from "@react-navigation/native";
import { Ionicons } from '@expo/vector-icons';

const Header = () => {
    const navigation = useNavigation();
    return (
        <View style={styles.header}>
            <TouchableOpacity onPress={() => navigation.dispatch(DrawerActions.openDrawer()) }>
                <Ionicons name="menu" size={24} color={"#1E7200"}/>
            </TouchableOpacity>

            <Image source={require("@/assets/images/logo.png") } style={styles.image}></Image>

            <TouchableOpacity>
                <Ionicons name="person" size={24} color={"#1E7200"}/>
            </TouchableOpacity>

        </View>
    )
}

const styles = StyleSheet.create(
    {
        header: {
            height: 80,
            backgroundColor: "white",
            paddingInline: 15,
            justifyContent: "space-between",
            alignItems: "center",
            flexDirection: "row",
            paddingTop: 15,
            elevation: 5
        },

        image: {
            width: 100,
            height: 100
        }

        

    }
)

export default Header