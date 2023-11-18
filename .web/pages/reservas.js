import { Fragment, useContext, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { Event, getAllLocalStorageItems, getRefValue, getRefValues, isTrue, preventDefault, refs, set_val, spreadArraysOrObjects, uploadFiles, useEventLoop } from "/utils/state"
import { ColorModeContext, EventLoopContext, initialEvents, StateContext } from "/utils/context.js"
import range from "/utils/helpers/range.js"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, Heading, HStack, Image, Input, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Modal, ModalBody, ModalContent, ModalHeader, ModalOverlay, option, Select, Spacer, Text, VStack } from "@chakra-ui/react"
import { getEventURL } from "/utils/state.js"
import NextLink from "next/link"
import { HamburgerIcon } from "@chakra-ui/icons"
import NextHead from "next/head"



export default function Component() {
  const state = useContext(StateContext)
  const router = useRouter()
  const [ colorMode, toggleColorMode ] = useContext(ColorModeContext)
  const focusRef = useRef();
  
  // Main event loop.
  const [addEvents, connectError] = useContext(EventLoopContext)

  // Set focus to the specified element.
  useEffect(() => {
    if (focusRef.current) {
      focusRef.current.focus();
    }
  })

  // Route after the initial page hydration.
  useEffect(() => {
    const change_complete = () => addEvents(initialEvents())
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Fragment>
  <Fragment>
  {isTrue(connectError !== null) ? (
  <Fragment>
  <Modal isOpen={connectError !== null}>
  <ModalOverlay>
  <ModalContent>
  <ModalHeader>
  {`Connection Error`}
</ModalHeader>
  <ModalBody>
  <Text>
  {`Cannot connect to server: `}
  {(connectError !== null) ? connectError.message : ''}
  {`. Check if server is reachable at `}
  {getEventURL().href}
</Text>
</ModalBody>
</ModalContent>
</ModalOverlay>
</Modal>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  <HStack alignItems={`flex-start`} sx={{"transition": "left 0.5s, width 0.5s", "position": "relative"}}>
  <Box sx={{"display": ["none", "none", "block"], "minWidth": "20em", "height": "100%", "position": "sticky", "top": "0px", "borderRight": "1px solid #F4F3F6"}}>
  <VStack sx={{"height": "100dvh"}}>
  <HStack sx={{"width": "100%", "borderBottom": "1px solid #F4F3F6", "padding": "1em"}}>
  <Image src={`/icon.png`} sx={{"height": "2em"}}/>
  <Spacer/>
  <Link as={NextLink} href={`https://github.com/basicallydanny/ProSem`}>
  <Center sx={{"boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "bg": "transparent", "borderRadius": "0.375rem", "Hover": {"bg": "#F5EFFE"}}}>
  <Image src={`/github.svg`} sx={{"height": "3em", "padding": "0.5em"}}/>
</Center>
</Link>
</HStack>
  <VStack alignItems={`flex-start`} sx={{"width": "100%", "overflowY": "auto", "padding": "1em"}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/menu") || (((state.router.page.path === "/") && "Menu") === "Menu")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/menu") || (((state.router.page.path === "/") && "Menu") === "Menu")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/.png`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Menu`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/inventario`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/inventario") || (((state.router.page.path === "/") && "Inventario") === "Menu")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/inventario") || (((state.router.page.path === "/") && "Inventario") === "Menu")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/inventario.png`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Inventario`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/proyecto`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/proyecto") || (((state.router.page.path === "/") && "Proyecto") === "Menu")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/proyecto") || (((state.router.page.path === "/") && "Proyecto") === "Menu")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/proyecto.png`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Proyecto`}
</Text>
</HStack>
</Link>
  <Link as={NextLink} href={`/reservas`} sx={{"width": "100%"}}>
  <HStack sx={{"bg": isTrue((state.router.page.path === "/reservas") || (((state.router.page.path === "/") && "Reservas") === "Menu")) ? `#F5EFFE` : `transparent`, "color": isTrue((state.router.page.path === "/reservas") || (((state.router.page.path === "/") && "Reservas") === "Menu")) ? `#1A1060` : `black`, "borderRadius": "0.375rem", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "width": "100%", "paddingX": "1em"}}>
  <Image src={`/reservas.png`} sx={{"height": "2.5em", "padding": "0.5em"}}/>
  <Text>
  {`Reservas`}
</Text>
</HStack>
</Link>
</VStack>
  <Spacer/>
</VStack>
</Box>
  <Box sx={{"paddingTop": "5em", "paddingX": ["auto", "2em"], "flex": "1"}}>
  <Box sx={{"alignItems": "flex-start", "boxShadow": "0px 0px 0px 1px rgba(84, 82, 95, 0.14)", "borderRadius": "0.375rem", "padding": "1em", "marginBottom": "2em"}}>
  <VStack>
  <Text>
  {`The number is ${state.number}`}
</Text>
  <Button onClick={(_e) => addEvents([Event("state.update", {})], (_e), {})}>
  {`Update Number`}
</Button>
  <Input onFocus={(_e0) => addEvents([Event("state.change_text", {text:_e0.target.value})], (_e0), {})} type={`text`} value={state.text}/>
  <Heading>
  {("I just bought a bunch of " + state.selected)}
</Heading>
  <Text>
  {`${state.selected} is going to the moon!`}
</Text>
  <Select onChange={(_e0) => addEvents([Event("state.set_selected", {value:_e0.target.value})], (_e0), {})} value={state.selected}>
  <option value={`BTC`}>
  {`BTC`}
</option>
  <option value={`ETH`}>
  {`ETH`}
</option>
  <option value={`LTC`}>
  {`LTC`}
</option>
  <option value={`DOGE`}>
  {`DOGE`}
</option>
</Select>
</VStack>
</Box>
</Box>
  <Box sx={{"position": "fixed", "right": "1.5em", "top": "1.5em", "zIndex": "500"}}>
  <Menu>
  <MenuButton sx={{"width": "3em", "height": "3em", "backgroundColor": "white", "border": "1px solid #F4F3F6", "borderRadius": "0.375rem"}}>
  <HamburgerIcon sx={{"size": "4em", "color": "black"}}/>
</MenuButton>
  <MenuList>
  <MenuItem sx={{"Hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/`} sx={{"width": "100%"}}>
  {`Menu`}
</Link>
</MenuItem>
  <MenuItem sx={{"Hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/inventario`} sx={{"width": "100%"}}>
  {`Inventario`}
</Link>
</MenuItem>
  <MenuItem sx={{"Hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/proyecto`} sx={{"width": "100%"}}>
  {`Proyecto`}
</Link>
</MenuItem>
  <MenuItem sx={{"Hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`/reservas`} sx={{"width": "100%"}}>
  {`Reservas`}
</Link>
</MenuItem>
  <MenuDivider/>
  <MenuItem sx={{"Hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`https://github.com/reflex-dev`} sx={{"width": "100%"}}>
  {`About`}
</Link>
</MenuItem>
  <MenuItem sx={{"Hover": {"bg": "#F5EFFE"}}}>
  <Link as={NextLink} href={`mailto:founders@=reflex.dev`} sx={{"width": "100%"}}>
  {`Contact`}
</Link>
</MenuItem>
</MenuList>
</Menu>
</Box>
</HStack>
  <NextHead>
  <title>
  {`Reservas`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
  <meta content={`width=device-width, shrink-to-fit=no, initial-scale=1`} name={`viewport`}/>
</NextHead>
</Fragment>
  )
}
