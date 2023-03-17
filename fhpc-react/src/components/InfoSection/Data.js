import { FaLess } from "react-icons/fa";
import DoggyLogo from '../../images/gooddoggy.svg'
import Mindfulness from '../../images/mindfulness.svg'
import Dog from '../../images/dog.svg'

export const HomeObjOne = {
    id: 'about',
    lightBg: false,
    lightText: true,
    lightTextDesc: true,
    datopLine: 'EXCEPTIONAL PET SERVICES',
    headline: 'Superior Pet Care Solutions',
    description: 'Experience unparalleled pet care and take advantage of our exclusive app for easy appointment scheduling and efficient pet management.',
    buttonLabel: 'Begin Now',
    imgStart: false,
    img: DoggyLogo,
    alt: 'ALTHOME',
    dark: true,
    primary: true,
    darkText: false
}

export const HomeObjTwo = {
    id: 'discover',
    lightBg: true,
    lightText: false,
    lightTextDesc: false,
    datopLine: 'DELIGHTED & CONTENT PETS',
    headline: "Your Pet's Preferred Choice",
    description: 'Discover outstanding pet care and benefit from our exclusive app, simplifying appointment scheduling and pet management for a seamless experience.',
    buttonLabel: 'Explore Gallery',
    imgStart: true,
    img: Dog,
    alt: 'ALTHOME',
    dark: false,
    primary: true,
    darkText: true
}

export const HomeObjThree = {
    id: 'about',
    lightBg: true,
    lightText: false,
    lightTextDesc: false,
    datopLine: 'IN TRUSTED HANDS',
    headline: 'Reputable & Trusted Pet Care Specialist',
    description: 'Experience exceptional pet boarding services with our dedicated professionals, and utilize our exclusive app for scheduling appointments, managing your bookings, and staying connected to your beloved pets.',
    buttonLabel: 'Read Reviews',
    imgStart: false,
    img: Mindfulness,
    alt: 'ALTHOME',
    dark: false,
    primary: true,
    darkText: false
}