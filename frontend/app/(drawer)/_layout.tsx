import { Drawer } from "expo-router/drawer";
import Header from "@/components/header/Header";
import { Ionicons } from "@expo/vector-icons";
import { GestureHandlerRootView } from "react-native-gesture-handler";

import { 
  DrawerContentComponentProps,
  DrawerContentScrollView, 
  DrawerItemList,
  DrawerItem
 } from "@react-navigation/drawer";

import { 
  Image,
  View,
  Text
 } from "react-native";

import { useRouter } from "expo-router";

const vascoDaGama = ( props: DrawerContentComponentProps ) => {

  const router = useRouter()

  return (
    <DrawerContentScrollView {...props}>
      <View style={{ padding: 16, alignItems: "center" }}>
        <Image source={require("@/assets/images/logo.png")} style={{ width: 250, height: 250 }}/>
      </View>

      <DrawerItemList {...props} />

      <View>
          <Text style={{fontSize: 16, fontWeight: "bold", marginBlock: 10}}>
            Instituições:
          </Text>
      </View>

      <DrawerItem label={"Escolas"} onPress={() => router.push("/(drawer)/pages/instituicoes/escolas")} icon={() => <Ionicons name="school" size={24}/>} />

      <DrawerItem label={"ONGs"} onPress={() => router.push("/(drawer)/pages/instituicoes/ongs")} icon={() => <Ionicons name="business" size={24}/>} />

      </DrawerContentScrollView>
  )
}

export default function RootLayout() {

  return (
    <GestureHandlerRootView style={{flex: 1}}>
      <Drawer
        drawerContent={vascoDaGama}
        screenOptions={{
          drawerHideStatusBarOnOpen: true,
          header: () => <Header />
        }}
      >;

        <Drawer.Screen 
          name="pages/home"
          options={{
            drawerLabel: "Home",
            drawerIcon: () => <Ionicons name="home" size={24} />
          }}
        />;

        <Drawer.Screen
          name="pages/profile"
          options={{
            drawerLabel: "Perfil",
            drawerIcon: () => <Ionicons name="person" size={24}/>
          }}
        />

        <Drawer.Screen
          name="pages/instituicoes/escolas"
          options={{
            drawerItemStyle: {
              display: "none"
            }
          }}
        />

        <Drawer.Screen
          name="pages/instituicoes/ongs"
          options={{
            drawerItemStyle: {
              display: "none"
            }
          }}
        />
      </Drawer>
    </GestureHandlerRootView>
  )
}
