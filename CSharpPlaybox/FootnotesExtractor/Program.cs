using DocumentFormat.OpenXml;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;

namespace FootnotesExtractor
{
    class Program
    {
        static void Main(string[] args)
        {
            string fileName = @"Salvatore Di Fazio.docx";
            using (WordprocessingDocument myDocument = WordprocessingDocument.Open(fileName, true))
            {
                var footnotesPart = myDocument.MainDocumentPart.FootnotesPart;
                if (footnotesPart != null)
                {
                    var footnotes = footnotesPart.Footnotes.Elements<Footnote>().Take(10);

                    foreach (var footnote in footnotes)
                    {
                        Console.WriteLine(footnote.InnerText);
                    }
                }
            }
            Console.WriteLine("All done. Press a key.");
            Console.ReadKey();
        }
    }
}
