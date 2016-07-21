package com.progoti.tools.converter;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Created by Nayan on 19 Jun, 2016
 */
public class BijoyToUnicodeConverterTest {

    @Test
    public void testRandomConversion() {

        assertEquals("ধামরাই, ঢাকা", BijoyToUnicodeConverter.convert("avgivB, XvKv"));
        assertEquals("প্রিয়া আক্তার", BijoyToUnicodeConverter.convert("wcÖqv Av³vi"));
        assertEquals("স্মৃতি", BijoyToUnicodeConverter.convert("¯§„wZ"));
        assertEquals( "শর্মিলা", BijoyToUnicodeConverter.convert("kwg©jv"));
        assertEquals(BijoyToUnicodeConverter.convert("¯^v¶i"), "স্বাক্ষর");
        assertEquals(BijoyToUnicodeConverter.convert("Zx¶è"), "তীক্ষ্ন");
        assertEquals(BijoyToUnicodeConverter.convert("j²Y"), "লক্ষ্ণণ");
        assertEquals(BijoyToUnicodeConverter.convert("†gvt"), "মোঃ");
        assertEquals(BijoyToUnicodeConverter.convert("ivóª"), "রাষ্ট্র");
        assertEquals(BijoyToUnicodeConverter.convert("eªþcyÎ"), "ব্রহ্মপুত্র");
        assertEquals(BijoyToUnicodeConverter.convert("Pvu`cyi"), "চাঁদপুর");
        assertEquals(BijoyToUnicodeConverter.convert("weÁvb"), "বিজ্ঞান");
        assertEquals(BijoyToUnicodeConverter.convert("PÂj"), "চঞ্চল");
        assertEquals(BijoyToUnicodeConverter.convert("wnZ cÖv_wgK"), "হিত প্রাথমিক");
        assertEquals(BijoyToUnicodeConverter.convert("M½v cÙv Ck¦i KY©dzjx `¤¢ cÖZ¨yrcYœgwZ wKsKZ©e¨weg~p iscyi"),
                "গঙ্গা পদ্মা ঈশ্বর কর্ণফুলী দম্ভ প্রত্যুৎপণ্নমতি কিংকর্তব্যবিমূঢ় রংপুর");

        assertEquals("মোবাইল নম্বর", BijoyToUnicodeConverter.convert("†gvevBj b¤^i"));
        assertEquals("জাতীয় পরিচয় পত্র নম্বর", BijoyToUnicodeConverter.convert("RvZxq cwiPq cÎ b¤^i"));
        assertEquals("১২২ নং চৌটাইল সরকারী প্রাথমিক বিদ্যালয়",
                BijoyToUnicodeConverter.convert("122 bs †PŠUvBj miKvix cÖv_wgK we`¨vjq"));

    }

    @Test(expected=NullPointerException.class)
    public void testNullPointerExceptionForNullInput() {
        assertEquals(BijoyToUnicodeConverter.convert(null), null);
    }

    @Test
    public void testNumberConversions(){
        assertEquals("১২৩৪৫৬৭৮৯০", BijoyToUnicodeConverter.convert("1234567890"));
        assertEquals("১২৩.১৫০১", BijoyToUnicodeConverter.convert("123.1501"));
    }

    @Test
    public void testEnglishConversions(){
        assertEquals("যবষষড়", BijoyToUnicodeConverter.convert("hello"));
    }

    @Test
    public void testUnicodeConversions(){
        assertEquals("ঝর্না রাজবংশী", BijoyToUnicodeConverter.convert("ঝর্না রাজবংশী"));
    }

    @Test
    public void testEmtyStringConversion(){
        assertEquals(BijoyToUnicodeConverter.convert(""), "");
    }
}
